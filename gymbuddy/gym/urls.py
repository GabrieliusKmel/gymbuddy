from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('advice/', views.ChatAdvice.as_view(), name='chatadvice'),
]
