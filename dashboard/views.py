from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



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
         form  = ProfileForm()
         context ['form'] =form
         return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':
        
        
        form= ProfileForm(request.POST)
       
            
        # form= ProfileForm(request.POST,instance= request.user.profile)
        # obj = form.save(commit=False)
        # obj.user = request.user
        # obj.save()
        if form.is_valid():
           form.save()
        return redirect('profile') 
    
    
            
    return render(request, 'dashboard/profile.html', context)
