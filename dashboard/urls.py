from django.urls import path

from . import views

urlpatterns = [
 
   path('home', views.home, name='dashboard'),
   path('/dashboard/profile', views.profile, name='profile'),
   
   
   
   
]