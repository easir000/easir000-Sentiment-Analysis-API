# from django.urls import path

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
 
   path('home', views.home, name='dashboard'),
   path('profile', views.profile, name='profile'),
   
   
   
   
]