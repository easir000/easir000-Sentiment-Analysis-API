from django.shortcuts import render ,redirect
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
        
        if not password1 == password2:
            messages.error(request,"password did not matches")
            return redirect ('register')
       
        if User.objects.filter(email=email).exists():
            messages.error (request,"A user with this email address : {} already exists, please use a different email".format(email))
       
        return redirect ('register')
    
        newUser = User.objects.create_user(email=email,username=email,password=password2)
        newUser.save()
        auth.login(request,user)
        return redirect ('home')
        # return HttpResponseRedirect (request,"authorisation/register.html", {})
        return render(request, 'register.html')
     