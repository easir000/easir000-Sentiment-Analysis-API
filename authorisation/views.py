from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.

def login(request):
    return render (request,'authorisation/login.html', {})

def register(request):
    if request.method == 'POST':
        
        email = request.POST ['email'].replace('','' ).lower()
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        
        # if not password1 == password2:
        #     messages.error(request,"password did not matches")
        #     return redirect ('register')
       
        # if User.objects.filter(email=email).exists():
        #     messages.error (request,"A user with this email address : {} already exists, please use a different email".format(email))
       
        # return redirect ('register')
    
        # newUser = User.objects.create_user(email=email,username=email,password=password2)
        # newUser.save()
        # auth.login(request,newUser)
        # return redirect ('home')
        # return render (request,'authorisation/register.html')
    
     
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                # user = User.objects.create_user(email=email,username=email,password=password2)
                # user.save()
				
                
                newUser = User.objects.create_user(email=email,username=email,password=password2)
                newUser.save()
                auth.login(request,newUser)
                return redirect ('home')
                
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render (request,'authorisation/register.html')