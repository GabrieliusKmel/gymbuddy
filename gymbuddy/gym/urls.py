from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('advice/', views.ChatAdvice.as_view(), name='chatadvice'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
]
