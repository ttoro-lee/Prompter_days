from django.shortcuts import render, redirect
from .forms import FriendForm
import openai
from django.conf import settings
from django.contrib import messages

def index(request):
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