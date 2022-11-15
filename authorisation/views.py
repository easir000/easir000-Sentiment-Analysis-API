from django.shortcuts import render ,redirect

# Create your views here.

def login(request):
    return render (request,'authorisation/login.html', {})

def register(request):
    if request.method == 'POST':
        email = request.post ['email']
        password = request.post ['password ']
        
       
        return redirect ('register')
        
    return render (request,'authorisation/register.html', {})