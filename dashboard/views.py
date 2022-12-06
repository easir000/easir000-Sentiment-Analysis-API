from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404

from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.views import View


from .models import *


from dashboard.forms import ProfileForm


@login_required
def home(request):
    
    context = {}    
    return render (request,'dashboard/home.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        
        p_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        
        p_form = ProfileForm(instance=request.user.profile)

    context = {
       
        'p_form': p_form
    }

    return render(request, 'dashboard/home.html', context)

# def profile(request):
#     context = {}  
   
#     if request.method == 'GET':
#         form  = ProfileForm(instance=request.user)
#         context ['form'] =form
#         return render(request, 'dashboard/profile.html', context)
    
    
#     if request.method == 'POST':
#         context['form'] = form
#         form= ProfileForm(request.POST,instance=request.user)
#         if form.is_valid():
#            form.save()
#         return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)


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
