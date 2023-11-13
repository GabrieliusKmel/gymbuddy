from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name="profile"),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('pdf/', views.GeneratePDF.as_view(), name='pdf'),
]