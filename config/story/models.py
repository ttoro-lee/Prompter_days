from django.db import models

# Create your models here.

class Story(models.Model):
    plus_text = models.CharField(max_length=200)