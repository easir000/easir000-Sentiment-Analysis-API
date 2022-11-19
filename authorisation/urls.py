from django.urls import path,logoutView

from . import views

urlpatterns = [
   path('login', views.login, name='login'),
   path('register', views.register, name='register'),
  path("logout", views.logout_request, name="logout"),
   
   
   
]