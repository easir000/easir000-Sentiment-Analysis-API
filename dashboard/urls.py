from django.urls import path
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views
from django.contrib import admin
urlpatterns = [
 
   path('home', views.home, name='dashboard'),
   path(r'^profile/', views.profile, name='profile'),
   
   
   
   
]