from django.contrib import admin

from .models import *



class Profile (admin.ModelAdmin):
    list_display = ['firstname','lastname','email','city']
    search_fields = ['firstname','lastname','email','city']
    list_per_page = 10
    
    




admin.site.register(Profile)






# Register your models here.
