from django.urls import path, include
from . import views

app_name = 'story'

urlpatterns = [
    path('', views.index, name='story'),
]