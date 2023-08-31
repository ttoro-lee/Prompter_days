from django.shortcuts import render, redirect
from .forms import FriendForm
import openai
import os, json
from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

# 프로젝트 루트로부터 secrets.json 파일 경로 찾기
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_env_variable(key):
    try:
        return secrets[key]
    except KeyError:
        error_msg = f"Set the {key} environment variable"
        raise ImproperlyConfigured(error_msg)

OPENAI_KEY = get_env_variable("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def index(request):
    # response = openai.Image.create(
    #     prompt="A Shiba Inu dog wearing a beret and black turtleneck",
    #     n=1,
    #     size="256x256"
    # )
    # image_url = response['data'][0]['url']
    # print(image_url)

    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['character_name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            likes = form.cleaned_data['likes']
            dislikes = form.cleaned_data['dislikes']

            context = {
                'name': name,
                'age': age,
                'gender': gender,
                'likes' : likes,
                'dislikes': dislikes,
            }
            return render(request,'setting_persona/chat.html', context)
        else:
            messages.info(request, '입력된 내용이 없습니다.')
            return redirect('setting_persona:setting_persona')
    else:
        form = FriendForm()
    return render(request, 'setting_persona/setting.html', {'form': form})


def chatting(request):
    return render(request, 'setting_persona/chat.html')