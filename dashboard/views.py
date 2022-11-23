from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .forms import *
from .models import *


@login_required
def home(request):
    
    context = {}    
    return render (request,'dashboard/home.html', context)


def profile(request):
    
    context = {}   
    # form = ProfileForm() 
    return render (request,'dashboard/profile.html', context)



