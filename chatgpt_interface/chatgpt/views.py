# views.py 
from django.shortcuts import render, redirect
from .models import GPTSub
from django.urls import reverse
from django.http import HttpResponse
from .forms import GPTRequestForm, get_model_choices, get_top_p_choices, get_temperature_choices
import openai


DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.9

def index(request):
    return HttpResponse("Hello, world. You're at the letters index.")


def handle_gpt_request(request):
    if request.method == 'POST':
        form = GPTRequestForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            temperature = float(form.cleaned_data.get('temperature') or DEFAULT_TEMPERATURE)
            top_p = float(form.cleaned_data.get('top_p') or DEFAULT_TOP_P)
            model = form.cleaned_data.get('model') or 'best'
            response_name = form.cleaned_data.get('response_name')
            num_tokens = form.cleaned_data.get('num_tokens')
            # Call GPT-3 API using prompt, temperature, top_p and model
            # and handle the response
            gpt_request = GPTSub.objects.create(prompt=prompt, temperature=temperature, top_p=top_p, model=model,response_name=response_name,num_tokens=num_tokens)
            return redirect('gpt_response', gpt_request.pk)
    else:
        form = GPTRequestForm()
    return render(request, 'gpt_template.html', {'form': form})


def handle_gpt_response(request, pk):
    gpt_response = GPTSub.objects.get(pk=pk)
    openai.api_key = "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"
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