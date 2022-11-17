from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages

# Create your views here.

def login(request):
    
    
    if request.method == 'POST':
        
        email = request.POST ['email'].replace('','' ).lower()
        password = request.POST ['password']
        # password2 = request.POST ['password2']
        
        user = auth.authenticate(username = email, password=password )
        
    
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request,'authorisation/login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'authorisation/login.html', {'form':form})
    
        
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
    
        # user = User.objects.create_user(email=email,username=email,password=password2)
        # user.save()
        # auth.login(request,user)
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
				
                
                user = User.objects.create_user(email=email,username=email,password=password2)
                user.save()
                auth.login(request,user)
                return redirect ('home')
                
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render (request,'authorisation/register.html')