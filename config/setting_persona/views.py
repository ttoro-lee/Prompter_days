from django.shortcuts import render
import openai
from django.conf import settings

def index(request):
    return render(request, 'setting_persona/setting.html')