from django.contrib import admin

from .models import *



class EasirAdmin (admin.ModelAdmin):
    list_display = ['firstname','lastname','email']
    search_fields = ['firstname','lastname','email']
    list_per_page = 10
    









# Register your models here.
