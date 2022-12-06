from django.contrib import admin

from .models import Profile



class ProfileAdmin (admin.ModelAdmin):
    list_display = ['firstname','lastname','email','city']
    search_fields = ['firstname','lastname','email','city']
    list_per_page = 10
    
    




admin.site.register(Profile,ProfileAdmin)






# Register your models here.
