from django.urls import path, include
from . import views

app_name = 'friend'

urlpatterns = [
    path('', views.index, name='friend'),
]