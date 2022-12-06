# from django.contrib import admin


# from .models import *



# admin.site.register(Profile)
# # Register your models here.


from django.contrib import admin

from .models import Profile



class Profile (admin.Model):
    list_display = ['firstname','lastname','email','city']
    search_fields = ['firstname','lastname','email','city']
    list_per_page = 10
    
    




admin.site.register(Profile)






# Register your models here.
