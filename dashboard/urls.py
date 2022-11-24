from django.urls import path

# from . import views
from django.contrib.auth import auth_views

urlpatterns = [
 
   path('home', auth_views.home, name='dashboard'),
   path('profile', auth_views.profile, name='profile'),
   
   
   
   
]