from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import FriendForm
import openai
import os, json
from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from config.settings import get_secret

OPENAI_KEY = get_secret("OPENAI_KEY")

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

def get_friend_image(request):
    response = openai.Image.create(
        prompt="illustration of cute, dog wearing hat and angry. child style",
        # tag를 받아오면, GPT-4 -> 하나의 번역된 문장으로 만들어줘 -> 달리2 이미지 생성
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    print(image_url)

    # 이미지 URL 반환
    return JsonResponse({"image_url": image_url})