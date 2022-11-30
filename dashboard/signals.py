from django.db.models.signals import post_save
from django.contrib.auth.models import User 
 
from django.dispatch import receiver

from dashboard.models import Profile

from .models import Profile  


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

# @receiver(pre_save, sender=User)

# def create_profile(sender, instance, created, **kwargs):
#     # ignore if this is an existing User
#     if created:
        
#      Profile.objects.create(user=instance)

# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs["created"]:
#         profile = Profile(user=user)
#         profile.save()
# post_save.connect(create_profile, sender=User)

    
    
#     # @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, **kwargs):
#     #  user = instance
#     # if created:
#     #     profile = Profile
#     #     profile.user = User
#     #     profile.save()
#         instance.profile.save()
# post_save.connect(create_profile, sender=User)
# post_save.connect(save_profile, sender=User)


