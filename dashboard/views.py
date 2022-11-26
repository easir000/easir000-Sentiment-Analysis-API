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



# @login_required
# def profile(request):
#     context = {}  
   
#     if request.method == 'GET':
#         form  = ProfileForm(instance = request.user.profile)
#         context ['form'] =form
#         # return render(request, 'dashboard/profile.html', context)
#     return render(request=request, template_name="dashboard/profile.html", context={"user":request.user,  "form":ProfileForm })
    
#     if request.method == 'POST':

#         form= ProfileForm(request.POST,instance = request.user.profile)
#         u = form.save()
#         profile = Profile.objects.create(user=u)
#         profile.save()
#         u.save()
#         return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form  = ProfileForm(instance = request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})