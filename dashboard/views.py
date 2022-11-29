from django.shortcuts import render ,redirect,HttpResponse 
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
    context['models'] = models
   
    # if request.method == 'GET':
    #     # form  = ProfileForm()
    #     context ['form'] =form
    #     return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':

        form= ProfileForm(request.POST)
        if form.is_valid():
         pass
    
    
        return render(request, 'dashboard/profile.html', context)