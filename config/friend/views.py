from django.shortcuts import render
import openai
from django.conf import settings

# Create your views here.
# def chatGPT(prompt, num):
#     openai.api_key = settings.OPENAI_KEY
#     model_name = 'gpt-3.5-turbo'

#     modified_prompt = prompt
#     # GPT 모델에 요청하여 출력 생성
#     response = openai.ChatCompletion.create(
#         model=model_name,
#         messages=[
#             {
#                 'role': 'system',
#                 'content': f'한국 인사담당자가 좋아하는 자기 소개서를 반드시 글자수 {num}자에 가깝게 끝나는 내용으로 생성'
#             },
#             {
#                 'role': 'user',
#                 'content': modified_prompt
#             }
#         ],
#         max_tokens=2048,
#         temperature=0.7
#     )

#     print(response)
#     result = response.choices[0].message.content.strip()
#     return result

def index(request):
    return render(request, 'friend/chat.html')

#def index(request):
#    return render(request, 'friend/layouts-without-navbar.html')