from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from django.templatetags.static import static


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
addressLine1 = models.CharField(null=True, blank=True, max_length=100)
addressLine2 = models.CharField(null=True, blank=True, max_length=100)
city = models.CharField(null=True, blank=True, max_length=100)
province = models.CharField(null=True, blank=True, max_length=100)
country = models.CharField(null=True, blank=True, max_length=100)
postalCode = models.CharField(null=True, blank=True, max_length=100)
# profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')

   
   
   
   
   
  
  
  
uniqueId = models.CharField(null=True, blank=True, max_length=100)
slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
date_created = models.DateTimeField(blank=True, null=True)
last_updated = models.DateTimeField(blank=True, null=True)

class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
