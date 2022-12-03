from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404


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
        if form.is_valid():
        #    form.save()
        # return redirect('profile') 
         pass
    
            
    return render(request, 'dashboard/profile.html', context)
# @login_required
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