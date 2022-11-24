from django.shortcuts import render ,redirect,HttpResponse

from django.contrib import messages
from django.contrib.auth.models import USer



from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import USer_passes_test


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
        form  = ProfileForm(instance = request.USer.profile)
        context ['form'] =form
        return render(request, 'dashboard/profile.html', context)
    
    
    
    if request.method == 'POST':
        form  =  ProfileForm(request.POST)

        if form.is_valid():
            
             form= ProfileForm(request.POST,instance = request.USer.profile)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    
    
            
    return render(request, 'dashboard/profile.html', context)
