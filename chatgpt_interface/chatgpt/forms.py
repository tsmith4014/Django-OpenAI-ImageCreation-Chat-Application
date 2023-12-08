# Forms
from django import forms
from .models import GPTSub
from .models import ImagePrompt

DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.9



def get_temperature_choices():
    return (
        (0.0, '0.0 - Least Creative'),
        (0.3, '0.3'),
        (0.5, '0.5'),
        (0.8, '0.8'),
        (1.0, '1.0 - Default Temperature'),
        (1.3, '1.3'),
        (1.5, '1.5'),
        (1.8, '1.8'),
        (2.0, '2.0 - Most Creative'),
    )

def get_top_p_choices():
    return (
        (0.0, '0.0 - Least Diverse'),
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
        (0.4, '0.4'),
        (0.5, '0.5 - Mid-Point'),
        (0.6, '0.6'),
        (0.7, '0.7'),
        (0.8, '0.8'),
        (0.9, '0.9 - Default Top P'),
        (1.0, '1.0 - Most Diverse'),
    )


def get_model_choices():
    return (
        ('gpt-3.5-turbo', '(gpt-3.5-turbo) - Blazingly Fast & inexpensive'),
    )

class GPTRequestForm(forms.ModelForm):
    class Meta:
        model = GPTSub
        fields = ['prompt', 'temperature', 'top_p', 'model', 'response_name']
    temperature = forms.ChoiceField(choices=get_temperature_choices(), initial=DEFAULT_TEMPERATURE)
    top_p = forms.ChoiceField(choices=get_top_p_choices(), initial=DEFAULT_TOP_P)
    model = forms.ChoiceField(choices=get_model_choices())

class EditGPTSubResponseForm(forms.ModelForm):
    class Meta:
        model = GPTSub
        fields = ['response', 'prompt']



class ImagePromptForm(forms.ModelForm):
    class Meta:
        model = ImagePrompt
        fields = ['prompt', 'n', 'size', 'response_format', 'model', 'quality', 'style']  # Include new fields






#old version below
# class ImagePromptForm(forms.ModelForm):
#     class Meta:
#         model = ImagePrompt
#         fields = ['prompt', 'n', 'size', 'response_format']



# class ImagePromptForm(forms.Form):
#     prompt = forms.CharField(widget=forms.Textarea)
#     n = forms.IntegerField()
#     size = forms.CharField(max_length=9, initial='1024x1024')
#     response_format = forms.CharField(max_length=12, initial='url')