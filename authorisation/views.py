from django.shortcuts import render ,redirect

# Create your views here.

def login(request):
    return render (request,'authorisation/login.html', {})

def register(request):
    if request.method == 'POST':
        username = request.post ['username']
        password = request.post ['password ']
        
        print ('Username Submitted Was : {}' .format(username))
        return redirect ('register')
        
    return render (request,'authorisation/register.html', {})