from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import RedirectView
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about', views.pricing, name='pricing')
   
   
]