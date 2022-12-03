from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.core.exceptions import ValidationError



from .forms import *
from .models import *





@login_required
def home(request):
    
    context = {}    
    return render (request,'dashboard/home.html', context)



# @login_required

def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'dashboard/profile.html', context)

def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, ValidationError(form))
        return redirect('profile')










# def profile(self,request):
#     context = {}  
   
#     if request.method == 'GET':
#         # form = ProfileForm(request.POST , instance=request.user.profile)
#         # context ['form'] =form
#         return render(request, 'dashboard/profile.html', context)
    
    
#     if request.method == 'POST':

#         form= ProfileForm(request.POST,instance=request.user.profile)
#         if form.is_valid():
#            form.save()
#         return redirect('profile') 
         
    
            
#     return render(request, 'dashboard/profile.html', context)
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