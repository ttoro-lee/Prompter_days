from django.urls import path

from . import views

app_name = 'dream'

urlpatterns = [
    path('', views.index, name='dream'),
]