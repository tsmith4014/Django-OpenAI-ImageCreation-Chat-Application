# views.py 
from django.shortcuts import render, redirect, get_object_or_404
from .models import GPTSub, ImagePrompt
from django.urls import reverse
from django.http import HttpResponse
from .forms import GPTRequestForm, get_model_choices, get_top_p_choices, get_temperature_choices, ImagePromptForm, EditGPTSubResponseForm
import openai 
import requests
import json
from decouple import config
import tiktoken

def num_tokens_from_messages(messages, model="gpt-3.5-turbo"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
        
    tokens_per_message = 4  # every message follows {role/name}\n{content}\n
    tokens_per_name = -1  # if there's a name, the role is omitted

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with assistant
    return num_tokens

# Example usage
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the weather today?"},
    {"role": "assistant", "content": "I'm sorry, I can't provide real-time information."},
]

print(f"{num_tokens_from_messages(messages)} prompt tokens counted.")


my_api_key = config('OPENAI_KEY')


DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.9


def index(request):
    if request.method == 'POST':
        if request.POST.get('gpt_sub_button'):
            return redirect('gpt_sub')
        elif request.POST.get('image_prompt_button'):
            return redirect('image_prompt')
    return render(request, 'index.html')



def handle_gpt_request(request):
    if request.method == 'POST':
        form = GPTRequestForm(request.POST)
        if form.is_valid():
            gpt_sub = form.save()
            
            headers = {
                "Authorization": "Bearer {}".format(my_api_key),
                "Content-Type": "application/json",
            }
            data = {
                "prompt": gpt_sub.prompt,
                "temperature": float(gpt_sub.temperature),
                "top_p": float(gpt_sub.top_p),
                "model": gpt_sub.model,
            }
            return redirect('gpt_response', gpt_sub.pk)
    else:
        form = GPTRequestForm()
    return render(request, 'gpt_template.html', {'form': form})


    
def handle_gpt_response(request, pk):
    gpt_response = GPTSub.objects.get(pk=pk)
    openai.api_key = my_api_key

    messages = [
        {
            "role": "system",
            "content": "This is a conversation with GPT-3.5-turbo."
        },
        {
            "role": "user",
            "content": gpt_response.prompt
        }
    ]

    # Calculate the tokens used by your prompt
    prompt_tokens = num_tokens_from_messages(messages, model=gpt_response.model)
    gpt_response.prompt_tokens = prompt_tokens

    # Subtract the tokens used by the prompt from the max token limit
    max_tokens_for_response = 4096 - prompt_tokens - 10  # added buffer for any extra tokens required by the model

    response = openai.ChatCompletion.create(
        model=gpt_response.model,
        messages=messages,
        temperature=float(gpt_response.temperature),
        max_tokens=max_tokens_for_response,
    )

    if response['choices']:
        gpt_response.response = response['choices'][0]['message']['content']
        response_tokens = num_tokens_from_messages([{'role': 'assistant', 'content': gpt_response.response}], model=gpt_response.model)
        gpt_response.response_tokens = response_tokens
        gpt_response.tokens_used = prompt_tokens + response_tokens
        gpt_response.save()

    return render(request, 'gpt_response.html', {'gpt_response': gpt_response})



def list_gpt_sub_responses(request):
    gpt_sub_responses = GPTSub.objects.all()
    print(gpt_sub_responses)
    return render(request, 'gpt_sub_response_list.html', {'gpt_sub_responses': gpt_sub_responses})


def edit_gpt_sub_response(request, pk):
    gpt_sub_response = GPTSub.objects.get(pk=pk)
    form = EditGPTSubResponseForm(request.POST or None, initial={'response': gpt_sub_response.response, 'prompt': gpt_sub_response.prompt})

    if request.method == 'POST':
        if form.is_valid():
            gpt_sub_response.response = form.cleaned_data['response']
            gpt_sub_response.prompt = form.cleaned_data['prompt']
            gpt_sub_response.save()
            return redirect('gpt_sub_response_list')

    return render(request, 'gpt_sub_response_edit.html', {'form': form})



def delete_gpt_sub_response(request, pk):
    gpt_sub_response = GPTSub.objects.get(pk=pk)
    if request.method == 'POST':
        gpt_sub_response.delete()
        return redirect('gpt_sub_response_list')
    return render(request, 'gpt_sub_response_confirm_delete.html', {'gpt_sub_response': gpt_sub_response})

#############################New DALL-E views below#############################################

# Function to call the DALL-E API
def generate_image(prompt, model='dall-e-3', n=1, size='1024x1024', quality='standard', style='vivid'):
    my_api_key = config('OPENAI_KEY')  # Retrieve API key from Django settings
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {my_api_key}'
    }
    data = {
        'prompt': prompt,
        'model': model,
        'n': n,
        'size': size,
        'quality': quality,
        'style': style
    }
    response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.json())
    return response.json()
    return response.json()

# View to handle image prompt request
def handle_image_prompt_request(request):
    if request.method == 'POST':
        form = ImagePromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            n = form.cleaned_data['n']
            size = form.cleaned_data['size']
            response_format = form.cleaned_data['response_format']
            model = form.cleaned_data.get('model', 'dall-e-3')
            quality = form.cleaned_data.get('quality', 'standard')
            style = form.cleaned_data.get('style', 'vivid')
            image_prompt = ImagePrompt.objects.create(
                prompt=prompt, n=n, size=size, response_format=response_format,
                model=model, quality=quality, style=style
            )
            return redirect('image_prompt_response', image_prompt.pk)
    else:
        form = ImagePromptForm()
    return render(request, 'image_prompt_template.html', {'form': form})

# View to handle image prompt response
def handle_image_prompt_response(request, pk):
    image_prompt_response = get_object_or_404(ImagePrompt, pk=pk)
    response_data = generate_image(
        prompt=image_prompt_response.prompt, 
        model=image_prompt_response.model, 
        n=image_prompt_response.n, 
        size=image_prompt_response.size, 
        quality=image_prompt_response.quality, 
        style=image_prompt_response.style
    )

    image_urls = [item['url'] for item in response_data.get('data', [])] if response_data else []
    print(image_urls)
    return render(request, 'image_prompt_response.html', {
        'image_prompt_response': image_prompt_response,
        'image_urls': image_urls
    })