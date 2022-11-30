from django.urls import path

from . import views

urlpatterns = [
 
   # path('home', views.home, name='dashboard'),
   path('profile', views.profile, name='profile'),
    path('profile/', views.profileView.as_view(), name='profile'),
   
   
   
   
]