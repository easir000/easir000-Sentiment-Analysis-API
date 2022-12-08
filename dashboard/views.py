from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404

from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

from .forms import *
from .models import *


@login_required
def home(request):
    
    context = {}    
    return render (request,'dashboard/home.html', context)



@login_required
def profile(request):
    context = {}  
   
    if request.method == 'GET':
        form  = ProfileForm(request.GET or None)
        image_form  = ProfileImageForm(request.GET or None)
                                   
        context ['form'] =form                          
        context ['image_form'] =image_form
        return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST or None)
        image_form  = ProfileImageForm(request.POST or None)
#        
        if form.is_valid():
           form.save()
        return redirect('profile') 
    
    if image_form.is_valid():
        image_form.save()
    return redirect('profile')
    
    return render(request, 'dashboard/profile.html', context)


# @login_required(login_url='login')
# def profile(request):
#     context = {}  
#     if request.method == "POST":
#         form = ProfileForm(request.POST , request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Your profile was successfully created!!'))
#         else:
#             messages.error(request, 'Error saving form')

#         return redirect("profile")
    
#     # else:
#     #     user = request.user
#     #     profile = user.profile
#     #     form = ProfileForm(instance=profile)

#     # context = {'form' : form}
#     return render(request , 'dashboard/profile.html' , context)
