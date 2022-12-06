from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
from django_resized import ResizedImageField
from django.db import models
from django.utils.translation import gettext as _
import os 

# Create your models here.
class Profile(models.Model):
    #Standard Variables
    
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
 user = models.OneToOneField(User,  on_delete=models.CASCADE)
addressLine1 = models.CharField(null=True, blank=True, max_length=100)
addressLine2 = models.CharField(null=True, blank=True, max_length=100)
city = models.CharField(null=True, blank=True, max_length=100)
province = models.CharField(null=True, blank=True, max_length=100)
country = models.CharField(null=True, blank=True, max_length=100)
postalCode = models.CharField(null=True, blank=True, max_length=100)
profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')

   
   
   
   
   
  
  
  
uniqueId = models.CharField(null=True, blank=True, max_length=100)
slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
date_created = models.DateTimeField(blank=True, null=True)
last_updated = models.DateTimeField(blank=True, null=True)

class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        
        
        