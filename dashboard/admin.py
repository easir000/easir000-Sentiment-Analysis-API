from django.contrib import admin


from .models import *

from dashboard.models import Profile

admin.site.register(Profile)
# Register your models here.
