from django.urls import path, include
from . import views

app_name = 'setting_persona'

urlpatterns = [
    path('', views.index, name='setting_persona'),
    path('chatting', views.chatting, name='chatting'),
]