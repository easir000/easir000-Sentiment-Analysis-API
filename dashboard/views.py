from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views import View


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect


from dashboard.forms import ProfileForm, form_validation_error

from dashboard.models import Profile
from django.utils.decorators import method_decorator




# @login_required
def home(request):
    
    context = {}    
    return render (request,'dashboard/home.html', context)



# @login_required
# def profile(request):
#     context = {}  
    
#     if request.method == 'GET':
#          form  = ProfileForm()
#          context ['form'] =form
#          return render(request, 'dashboard/profile.html', context)
    
    
#     if request.method == 'POST':
        
        
#         form= ProfileForm(request.POST)
       
            
#         # form= ProfileForm(request.POST,instance= request.user.profile)
#         # obj = form.save(commit=False)
#         # obj.user = request.user
#         # obj.save()
#         if form.is_valid():
#            form.save()
#         return redirect('profile') 
    
    
            
#     return render(request, 'dashboard/profile.html', context)

# @login_required
# def profile(request):
    
#     form  = ProfileForm(request.POST or None)
#     if  form.is_valid():
#         form.save()
#         messages.success(request,'Your profile has been updated successfully')
            
#         return HttpResponseRedirect('profile')
#     context = {
                
#                 'form': form
#             }
#     return render(request, 'dashboard/profile.html', context)

# def profile(request):
#     context = {}  
    
#     if request.method == 'GET':
#          form  = ProfileForm(instance=request.user.profile)
#          context ['form'] =form
#          return render(request, 'dashboard/profile.html', context)

#     if request.method == 'POST': 
#      form = ProfileForm(
#             request.POST,
#             # request.FILES,
#             instance=request.user.profile
#         )

#     if  form.is_valid():
            
#         form.save()
            
#         messages.success(request,'Your profile has been updated successfully')
            
#         return redirect('profile')
#     else:
#             context = {
                
#                 'form': form
#             }
#             messages.error(request,'Error updating you profile')
            
#     return render(request, 'dashboard/profile.html', context)
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

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
            messages.error(request, form_validation_error(form))
        return redirect('profile')
        return render(request, 'dashboard/profile.html', context)