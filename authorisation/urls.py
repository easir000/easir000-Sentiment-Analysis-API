from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import RedirectView
from . import views

urlpatterns = [
   path('login', views.login, name='login'),
   path('register', views.register, name='register'),
   
   
]