

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib import messages





from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def login(request):
    

    msg = None

    if request.method == "POST":

        email = request.POST ['email'].replace('','' ).lower()
        password = request.POST['password']
        user = auth.authenticate( username = email, password = password)
        
        if user is not None:
                 auth.login(request, user)
                 return redirect('dashboard')
        else:
                msg = 'Invalid credentials'
    else:
            msg = 'Error validating the form'

            return redirect('register')
    return render (request,'authorisation/login.html', {})

def register(request):
    msg = None
    success = False

    if request.method == "POST":
        email = request.POST ['email'].replace('','' ).lower()
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        
    if password1 and password2 and password1 != password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('register')
             
            else:
               
              user = authenticate(email=email,username=email,password=password2)
              user.save()
            auth.login(request,user)
            return redirect ('dashboard')
                
             
          
          
    else:
        return render (request,'authorisation/register.html' )
    
   #using the long-required decorator
@login_required
def logout(request):
  auth.logout(request)
  return redirect('login')