from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout


from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
 



LOGGED_IN_HOME = settings.LOGGED_IN_HOME

def login_forbidden(function=None, redirect_field_name=None, redirect_to=LOGGED_IN_HOME):
    """
    Decorator for views that checks that the user is NOT logged in, redirecting
    to the homepage if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated(),
        login_url=redirect_to,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator



# def anonymous_required(function=None, redirect_url=None):
#     if not redirect_url:
#         redirect_url = 'dashboard'

#     actual_decorator = user_passes_test(
#         lambda u: u.is_anonymous(),
#         login_url=redirect_url
#     )

#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# @anonymous_required
@login_forbidden
def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        email = request.POST ['email'].replace('','' ).lower()
        password = request.POST['password']
        user = auth.authenticate(request, username = email, password = password)
        if user:
            auth.login(request, user)
            messages.success(request, f' welcome {user} !!')
            return redirect('dashboard')
        else:
            messages.error(request, f'account does not exit plz sign in')
    
    return render (request,'authorisation/login.html', {})

# @anonymous_required
@login_forbidden
def register(request):
    if request.method == 'POST':
        
        email = request.POST ['email'].replace('','' ).lower()
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        
      
    
     
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('register')
             
            else:
                # user = User.objects.create_user(email=email,username=email,password=password2)
                # user.save()
				
                
                user = User.objects.create_user(email=email,username=email,password=password2)
                user.save()
                auth.login(request,user)
                return redirect ('dashboard')
                
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render (request,'authorisation/register.html' )
    
    @login_required 
    def logout_request(request):
     logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")