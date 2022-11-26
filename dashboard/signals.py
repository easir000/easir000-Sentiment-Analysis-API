from django.db.models.signals import post_save,pre_delete,pre_save,post_delete
from django.contrib.auth.models import User

from django.dispatch import receiver
from .models import Profile  

@receiver(pre_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver([post_save,post_delete], sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     instance.profile.save()
    
    
    @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    def save_profile(sender, instance, created, **kwargs):
     user = instance
    if created:
        profile = Profile(user=User)
        profile.save()
        
    post_save.connect(create_profile, sender=User)
    post_save.connect(save_profile, sender=User)