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



# @login_required
# def profile(request):
#     context = {}  
   
#     if request.method == 'GET':
#         form  = ProfileForm(instance = request.user.profile)
#         context ['form'] =form
#         return render(request, 'dashboard/profile.html', context)
    
    
#     if request.method == 'POST':
#         context['form'] = form
#         form= ProfileForm(request.POST,instance = request.user.profile)
#         if form.is_valid():
#            form.save()
#         return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        user_account_form = ProfileForm(request.POST , request.FILES, instance=request.user.profile)
        if user_account_form.is_valid():
            user_account_form.save()
            messages.success(request, ('Your profile was successfully created!!'))
        else:
            messages.error(request, 'Error saving form')

        return redirect("http://127.0.0.1:8000/")
    
    else:
        user = request.user
        profile = user.profile
        user_account_form = ProfileForm(instance=profile)

    context = {'form' : user_account_form}
    return render(request , 'dashboard/profile.html' , context)
