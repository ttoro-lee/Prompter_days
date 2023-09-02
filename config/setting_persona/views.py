from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import FriendForm
import openai
import os, json, requests, base64
from pathlib import Path
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from config.settings import get_secret

OPENAI_KEY = get_secret("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def index(request):

    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            canvas_image_data = form.cleaned_data['canvas_image']  # 이미지 데이터 가져오기
            
            
            # 이미지 처리 로직 (예: 이미지 저장 등)
            
            # 다른 form 데이터 처리
            name = form.cleaned_data['character_name']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            likes = form.cleaned_data['likes']
            dislikes = form.cleaned_data['dislikes']
            
            # 새로운 HTML 페이지 렌더링
            context = {
                'name': name,
                'age': age,
                'gender': gender,
                'likes': likes,
                'dislikes': dislikes,
                'canvas_image_data': canvas_image_data,  # 이미지 데이터를 context에 추가
                # 필요한 다른 데이터를 context에 추가
            }
            return render(request, 'setting_persona/chat.html', context)
        else:
            messages.info(request, '입력된 내용이 없습니다.')
            #return render(request, 'setting_persona/setting.html', {'form' : form})
            #return redirect('setting_persona:setting_persona')
    else:
        form = FriendForm()
    return render(request, 'setting_persona/setting.html', {'form': form})


# def get_friend_image(request):
#     response = openai.Image.create(
#         prompt="illustration of cute, dog wearing hat and angry. child style",
#         # tag를 받아오면, GPT-4 -> 하나의 번역된 문장으로 만들어줘 -> 달리2 이미지 생성
#         n=1,
#         size="256x256"
#     )
#     image_url = response['data'][0]['url']

#     response = requests.get(image_url)
#     data_uri = 'data:image/jpeg;base64,' + base64.b64encode(response.content).decode('utf-8')

#     # data_uri = '<img src="data:image/png;base64,' + data_uri + '"  alt="' + prompt + '" />'
#     # 이미지 URL 반환
#     return JsonResponse({"image_url": data_uri})

def get_friend_image(request):
    
    # JavaScript에서 전달한 데이터 받기
    data = json.loads(request.body)
    name = data.get('name')
    clothes = data.get('clothes')
    emotion = data.get('emotion')

    input_text = f"귀여운 일러스트,  {name}가 {clothes}를 입고 있고 {emotion}한 표정, 어린이 그림체, 고퀄리티"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that translates text."},
        {"role": "user", "content": input_text},
    ]
    )

    translated_text = response['choices'][0]['message']['content']
    print("번역 결과:", translated_text)

    response = openai.Image.create(

        prompt = translated_text,
        # tag를 받아오면, GPT-4 -> 하나의 번역된 문장으로 만들어줘 -> 달리2 이미지 생성
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']

    response = requests.get(image_url)
    data_uri = 'data:image/jpeg;base64,' + base64.b64encode(response.content).decode('utf-8')

    # data_uri = '<img src="data:image/png;base64,' + data_uri + '"  alt="' + prompt + '" />'
    # 이미지 URL 반환
    return JsonResponse({"image_url": data_uri})

def get_sensitive_data(request):
    # secrets.json 파일 읽어오기
    with open('secrets.json') as f:
        secrets = json.load(f)
    
    # 클라이언트에게 민감한 정보 전달
    response_data = {
        'api_key': secrets['OPENAI_KEY'],
    }
    
    return JsonResponse(response_data)

