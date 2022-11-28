from django.shortcuts import render ,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.forms import ModelForm

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
def profile(request):
    context = {}  
   
    if request.method == 'GET':
        form  = ProfileForm(instance = request.user.profile)
        context ['form'] =form
        return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':

        form= ProfileForm(request.POST,instance = request.user.profile)
        if form.is_valid():
           form.save()
        return redirect('profile') 
    
    
            
    return render(request, 'dashboard/profile.html', context)


def dashboard(request):
    return render(request,"dashboard.html")

@login_required(login_url="user:login")
def get_profile(request):    
    
    profile = get_object_or_404(Profile,user=request.user)
    
    return render(request,"profile.html",{"profile":profile})

# @login_required(login_url="user:login")
def update_profile(request):       
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile is updated successfully")
            return HttpResponseRedirect(reverse("profile:profile"))   
        else:
            return render(request,"profile.html",{"form":form})                 
            
    return render(request,"edit.html",{"form":form})
