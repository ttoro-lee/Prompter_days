from django.shortcuts import render
import openai
from django.conf import settings

def index(request):
    return render(request, 'story/write.html')