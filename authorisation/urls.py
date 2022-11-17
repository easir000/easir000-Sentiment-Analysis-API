from django.urls import path
from django.contrib.auth import auth_views

from . import views

# urlpatterns = [
#    path('login', views.login, name='login'),
#    path('register', views.register, name='register'),
   
   
# ]


urlpatterns = [


   path('register', views.register, name='register'),
   
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

]