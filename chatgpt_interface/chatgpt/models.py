# models.py
from django.db import models

class GPTSub(models.Model):
    prompt = models.TextField()
    temperature = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    top_p = models.DecimalField(max_digits=3, decimal_places=2, default=0.9)
    model = models.CharField(max_length=255)  
    num_tokens = models.IntegerField()
    response_name = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.prompt

        
class ImagePrompt(models.Model):
    prompt = models.TextField(max_length=1000)
    n = models.PositiveSmallIntegerField(default=1)
    size = models.CharField(max_length=9, default='1024x1024')
    response_format = models.CharField(max_length=12, default='url')


    def __str__(self):
        return self.prompt

