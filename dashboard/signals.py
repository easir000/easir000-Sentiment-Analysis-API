from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver
from .models import Profile  

# @receiver(pre_save, sender=User)

def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    Profile.objects.create(user=instance)



    
    
    # @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, **kwargs):
    #  user = instance
    # if created:
    #     profile = Profile
    #     profile.user = User
    #     profile.save()
        instance.profile.save()
post_save.connect(create_profile, sender=User)
post_save.connect(save_profile, sender=User)


def update_user_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile.objects.create(user =instance)