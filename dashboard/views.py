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
    profile = User.profile
    if request.method == 'GET':
         form  = ProfileForm()
         context ['form'] =form
         return render(request, 'dashboard/profile.html', context)
    
    
    if request.method == 'POST':
        
        
        form= ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
    else:
            messages.error(request, (form))
    return redirect('profile')
            
        # form= ProfileForm(request.POST,instance= request.user.profile)
        # obj = form.save(commit=False)
        # obj.user = request.user
        # obj.save()
    #     if form.is_valid():
    #        form.save()
    #     return redirect('profile') 
    
    
            
    return render(request, 'dashboard/profile.html', context)
