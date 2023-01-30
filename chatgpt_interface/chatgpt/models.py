# models.py
from django.db import models

class GPTSub(models.Model):
    prompt = models.TextField()
    temperature = models.DecimalField(max_digits=2, decimal_places=1)
    top_p = models.DecimalField(max_digits=3, decimal_places=2)
    model = models.CharField(max_length=255)  #choices=get_model_choices()
    num_tokens = models.IntegerField()
    response_name = models.CharField(max_length=255)
    response = models.CharField(max_length=10000)

    def __str__(self):
        return self.prompt

        
class ImagePrompt(models.Model):
    prompt = models.TextField(max_length=1000)
    n = models.PositiveSmallIntegerField(default=1)
    size = models.CharField(max_length=9, default='1024x1024')
    response_format = models.CharField(max_length=12, default='url')


    def __str__(self):
        return self.prompt













# class ImageSub(models.Model):
#     prompt = models.TextField()
#     n = RangeIntegerField(min_value=1, max_value=10)
#     size = models.CharField(max_length=10)