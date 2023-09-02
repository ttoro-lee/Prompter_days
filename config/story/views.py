from django.shortcuts import render, redirect
import openai
from django.conf import settings
import io, os
from google.cloud import vision
from django.contrib import messages
from .forms import StoryForm
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

# def index(request):
#     return render(request, 'story/write.html')

def index(request):

    client = vision.ImageAnnotatorClient()

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            canvas_image_data = form.cleaned_data['canvas_image']  # 이미지 데이터 가져오기
            # 이미지 처리 로직 (예: 이미지 저장 등)
            print(canvas_image_data)
            image_data = base64.b64decode(canvas_image_data.split(',')[1])
            image = Image.open(BytesIO(image_data))
            image = np.array(image)
            print(image)
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # image = vision.Image(content=image)

            print(image)

            response = client.label_detection(image=image)
            labels = response.label_annotations

            print('Labels:')
            for label in labels:
                print(label.description)
            
            # 다른 form 데이터 처리
            plus_text = form.cleaned_data['plus_text']
            print(plus_text)
            
            # 새로운 HTML 페이지 렌더링
            context = {
                'plus_text': plus_text,
                'canvas_image_data': canvas_image_data,  # 이미지 데이터를 context에 추가
                # 필요한 다른 데이터를 context에 추가
                'form': form
            }
            return render(request, 'story/write.html', context)
        else:
            messages.info(request, '입력된 내용이 없습니다.')
            return redirect('story:story')
    else:
        form = StoryForm()
    return render(request, 'story/write.html', {'form': form})