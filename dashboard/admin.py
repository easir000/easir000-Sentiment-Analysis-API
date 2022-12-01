from django.contrib import admin


from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email')

admin.site.register(Profile, ProfileAdmin)


admin.site.register(Profile)
# Register your models here.
