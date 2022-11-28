from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model



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
#     # return render(request=request, template_name="dashboard/profile.html", context={"user":request.user,  "form":ProfileForm })
    
#     if request.method == 'POST':

#         form= ProfileForm(request.POST,instance = request.user.profile)
#         u = form.save()
#         profile = Profile.objects.create(user=u)
#         profile.save()
#         u.save()
#         return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)
def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = ProfileForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'users/profile.html', context={'form': form})

    return redirect("homepage")