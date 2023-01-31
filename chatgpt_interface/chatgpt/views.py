# views.py 
from django.shortcuts import render, redirect, get_object_or_404
from .models import GPTSub, ImagePrompt
from django.urls import reverse
from django.http import HttpResponse
from .forms import GPTRequestForm, get_model_choices, get_top_p_choices, get_temperature_choices, ImagePromptForm, EditGPTSubResponseForm
import openai 
import requests
import json

my_api_key = "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"


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
            gpt_sub = form.save(commit=False)
            prompt = gpt_sub.prompt
            temperature = gpt_sub.temperature
            top_p = gpt_sub.top_p
            model = gpt_sub.model
            num_tokens = gpt_sub.num_tokens
            response_name = gpt_sub.response_name
            gpt_sub.save()
            
            headers = {
                "Authorization": "Bearer {}".format(my_api_key),
                "Content-Type": "application/json",
            }
            data = {
                "prompt": prompt,
                "temperature": float(temperature),
                "top_p": float(top_p),
                "model": model,
                "max_tokens": int(num_tokens),
            }

            gpt_request = GPTSub.objects.create(prompt=prompt, temperature=temperature, top_p=top_p, model=model,response_name=response_name,num_tokens=num_tokens)
            return redirect('gpt_response', gpt_request.pk)
    else:
        form = GPTRequestForm()
    return render(request, 'gpt_template.html', {'form': form})


def handle_gpt_response(request, pk):
    gpt_response = GPTSub.objects.get(pk=pk)
    openai.api_key = my_api_key
    response = openai.Completion.create(
        engine=gpt_response.model,
        prompt=gpt_response.prompt,
        temperature=float(gpt_response.temperature),
        top_p=float(gpt_response.top_p),
        max_tokens=gpt_response.num_tokens,
    )
    gpt_response.response = response["choices"][0]["text"]
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


##########################################################################


def handle_image_prompt_request(request):
    if request.method == 'POST':
        form = ImagePromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            n = form.cleaned_data['n']
            size = form.cleaned_data['size']
            response_format = form.cleaned_data['response_format']
            # Call GPT-3 API using prompt
            # and handle the response
            image_prompt = ImagePrompt.objects.create(prompt=prompt, n=n, size=size, response_format=response_format)
            return redirect('image_prompt_response', image_prompt.pk)
    else:
        form = ImagePromptForm()
    return render(request, 'image_prompt_template.html', {'form': form})



def handle_image_prompt_response(request, pk):
    image_prompt_response = ImagePrompt.objects.get(pk=pk)
    print(image_prompt_response, 'this is the image_prompt_response')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {my_api_key}'
    }

    data = {
        'prompt': image_prompt_response.prompt,
        'n': image_prompt_response.n,
        'size': image_prompt_response.size
    }

    response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=json.dumps(data))
    response_data = response.json()
    image_urls = [item['url'] for item in response_data['data']]
    return render(request, 'image_prompt_response.html', {'image_prompt_response': image_prompt_response, 'image_urls': image_urls})





    # def edit_gpt_sub_response(request, pk):
#     gpt_sub_response = GPTSub.objects.get(id=pk)
#     if request.method == 'POST':
#         form = GPTRequestForm(request.POST, instance=gpt_sub_response)
#         if form.is_valid():
#             form.save()
#             return redirect('gpt_sub_response_list')
#     else:
#         form = GPTRequestForm(instance=gpt_sub_response)
#     return render(request, 'gpt_sub_response_edit.html', {'form': form})