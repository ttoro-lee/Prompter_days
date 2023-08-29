from django.db import models

# Create your models here.

class Friend(models.Model):
    character_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    likes = models.CharField(max_length=100)
    dislikes = models.CharField(max_length=300)