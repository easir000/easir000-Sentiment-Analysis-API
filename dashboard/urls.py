# from django.urls import path

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
 
   path('home', views.home, name='dashboard'),
   path('profile', views.profile, name='profile'),
   
   path('delete-blog-topic/<str:uniqueId>/', views.deleteBlogTopic, name='delete-blog-topic'),
   path('generate-blog-from-topic/<str:uniqueId>/', views.createBlogFromTopic, name='generate-blog-from-topic'),
   
  
   #Blog Generation Routes 
   path('generate-blog-topic', views.blogTopic, name='blog-topic'),
   path('generate-blog-sections', views.blogSections, name='blog-sections'),
   
   #Saving the blog topic for future resue
   path('save-blog-topic/<str:blogTopic>/', views.saveBlogTopic, name='save-blog-topic'),
   
   path('use-blog-topic/<str:blogTopic>/', views.useBlogTopic, name='use-blog-topic'),
   path('view-generated-blog/<slug:slug>/', views.viewGeneratedBlog, name='view-generated-blog'),
   
   path('billing', views.billing, name='billing'),
   path('534dac52-731d-439d-ac5f-773b29a9bfa4', views.webhook, name='webhook'),
   
   path('paypal-payment-success', views.PaypalPaymentSuccess, name='payment-success'),
   
   
   
   
   
   
]