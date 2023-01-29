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


