from django.urls import path, include
from . import views

app_name = 'setting_persona'

urlpatterns = [
    path('', views.index, name='setting_persona'),
    path('get_friend_image/', views.get_friend_image, name='get_friend_image'),
    path('get_sensitive_data/', views.get_sensitive_data, name='get_sensitive_data'),
]