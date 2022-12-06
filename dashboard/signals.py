from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver

from .models import Profile  


# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')



def create_profile(sender, instance, created, **kwargs):
    if created:
        
        Profile.objects.create(user=instance)
        # profile = Profile(user=instance)
        # profile.save()
        
def save_profile(sender, instance,  **kwargs):
    
        
        instance.profile.save()
        
post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)