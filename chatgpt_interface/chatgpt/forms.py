# Forms
from django import forms


DEFAULT_TEMPERATURE = 1.0
DEFAULT_TOP_P = 0.9


def get_temperature_choices():
    return (
        (0.0, '0.0 - Least Creative'),
        (0.25, '0.25'),
        (0.5, '0.5'),
        (0.75, '0.75'),
        (1.0, '1.0'),
        (1.25, '1.25'),
        (1.5, '1.5'),
        (1.75, '1.75'),
        (2.0, '2.0 - Most Creative'),
    )

def get_top_p_choices():
    return (
        (0.0, '0.0 - Least Diverse'),
        (0.1, '0.1'),
        (0.2, '0.2'),
        (0.3, '0.3'),
        (0.4, '0.4'),
        (0.5, '0.5- Mid-Point'),
        (0.6, '0.6'),
        (0.7, '0.7'),
        (0.8, '0.8'),
        (0.9, '0.9'),
        (1.0, '1.0 - Most Diverse'),
    )




def get_model_choices():
    return (
        ('text-davinci-002', 'Davinci-002'),
        ('code-davinci-002', 'Code Generation 8000 MAX Tokens'),
        ('text-davinci-003', 'Best Overall 4000 MAX Tokens'),
    )


class GPTRequestForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea)
    temperature = forms.ChoiceField(choices=get_temperature_choices(), initial=DEFAULT_TEMPERATURE)
    top_p = forms.ChoiceField(choices=get_top_p_choices(), initial=DEFAULT_TOP_P)
    response_name = forms.CharField(max_length=255)
    num_tokens = forms.IntegerField()
    model = forms.ChoiceField(choices=get_model_choices())



class ImagePromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea)
    n = forms.IntegerField()
    size = forms.CharField(max_length=9, initial='1024x1024')
    response_format = forms.CharField(max_length=12, initial='url')




class EditGPTSubResponseForm(forms.Form):
    # prompt = forms.CharField(max_length=100)
    prompt = forms.CharField(max_length=50)
    response = forms.CharField(
        label='Sub Response',
        widget=forms.Textarea,
        max_length=1024
    )
