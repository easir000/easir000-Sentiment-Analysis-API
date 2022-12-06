from django.urls import path

from dashboard import views

urlpatterns = [
 
   path('home', views.home, name='dashboard'),
   path('profile/', views.ProfileView.as_view(), name='profile'),
   
   
   
   
]