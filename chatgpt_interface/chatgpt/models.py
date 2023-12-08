# models.py
from django.db import models

class GPTSub(models.Model):
    prompt = models.TextField()
    temperature = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    top_p = models.DecimalField(max_digits=3, decimal_places=2, default=0.9)
    model = models.CharField(max_length=255)  
    response_name = models.CharField(max_length=255)
    response = models.TextField()
    tokens_used = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    prompt_tokens = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    response_tokens = models.DecimalField(max_digits=5, decimal_places=0, default=0)

    def __str__(self):
        return self.prompt



class ImagePrompt(models.Model):
    prompt = models.TextField(max_length=1000)
    n = models.PositiveSmallIntegerField(default=1)
    size = models.CharField(max_length=9, default='1024x1024')
    response_format = models.CharField(max_length=12, default='url')
    model = models.CharField(max_length=10, default='dall-e-3')  # New field for model
    quality = models.CharField(max_length=10, default='standard')  # New field for quality
    style = models.CharField(max_length=10, default='vivid')  # New field for style

    def __str__(self):
        return self.prompt




#old version below        
# class ImagePrompt(models.Model):
#     prompt = models.TextField(max_length=1000)
#     n = models.PositiveSmallIntegerField(default=1)
#     size = models.CharField(max_length=9, default='1024x1024')
#     response_format = models.CharField(max_length=12, default='url')


#     def __str__(self):
#         return self.prompt


