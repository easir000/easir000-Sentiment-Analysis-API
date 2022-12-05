from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

from .forms import NewUserForm, UserForm, ProfileForm
from .models import *





@login_required
def home(request):
    
    context = {} 
       
    return render (request,'dashboard/home.html', context)



# @login_required

def profile(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="dashboard/profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })


# def profile(request):
#     context = {}  
   
#     if request.method == 'GET':
#         form  = ProfileForm(instance = request.user.profile)
#         context ['form'] =form
#         return render(request, 'dashboard/profile.html', context)
    
    
# if request.method == 'POST':

#         form= ProfileForm(request.POST,instance = request.user.profile)
#         if form.is_valid():
#            form.save()
#     return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)
