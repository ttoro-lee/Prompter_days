from django.shortcuts import render, redirect
import openai
from django.conf import settings
import io, os
from google.cloud import vision
from django.contrib import messages
from .forms import StoryForm
import base64
from io import BytesIO
from config.settings import get_secret

# def index(request):
#     return render(request, 'story/write.html')

OPENAI_KEY = get_secret("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def index(request):

    client = vision.ImageAnnotatorClient()

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            canvas_image_data = form.cleaned_data['canvas_image']  # 이미지 데이터 가져오기
            # 이미지 처리 로직 (예: 이미지 저장 등)
            image_data = base64.b64decode(canvas_image_data.split(',')[1])
            image = BytesIO(image_data)

            response = client.label_detection(image=image)
            labels = response.label_annotations

            keywords = []
            bad_keywords = ['Cartoon', 'Snapshot', 'Cg artwork']
            for label in labels:
                if label.description not in bad_keywords:
                    keywords.append(label.description)

            print(','.join(keywords))

            # 다른 form 데이터 처리
            plus_text = form.cleaned_data['plus_text']

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a skilled English translator."},
                    {"role": "user", "content": f"Translate {plus_text} into English"},
                ]
            )

            translated_text = response['choices'][0]['message']['content']
            print("번역 결과:", translated_text)   
            
            fairytale = ','.join(keywords) + ',' + translated_text
            print(fairytale)

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a skilled Korean fairy tale writer. Write it naturally within ten sentences."},
                    {"role": "user", "content": f"Write a children's fairy tale based on {fairytale} in Korean"},
                ]
            )

            fairytale = response['choices'][0]['message']['content']
            print("동화:", fairytale)  
            
            # 새로운 HTML 페이지 렌더링
            context = {
                'fairytale': fairytale,
                'canvas_image_data': canvas_image_data,  # 이미지 데이터를 context에 추가
                # 필요한 다른 데이터를 context에 추가
                'form': form,
            }
            return render(request, 'story/result.html', context)
        else:
            messages.info(request, '입력된 내용이 없습니다.')
            return redirect('story:story')
    else:
        form = StoryForm()
    return render(request, 'story/write.html', {'form': form})
