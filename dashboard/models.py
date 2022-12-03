from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
from django_resized import ResizedImageField
from django.utils.translation import gettext as _
import os 

# Create your models here.
class Profile(models.Model):
    #Standard Variables
    
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   
addressLine1 = models.CharField(null=True, blank=True, max_length=100)
addressLine2 = models.CharField(null=True, blank=True, max_length=100)
city = models.CharField(null=True, blank=True, max_length=100)
province = models.CharField(null=True, blank=True, max_length=100)
country = models.CharField(null=True, blank=True, max_length=100)
postalCode = models.CharField(null=True, blank=True, max_length=100)
profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')

   
   
   
   
   
  
    #### ADD OTHER VARIABLES HERE
    
    
    #Related Variables
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable
  
uniqueId = models.CharField(null=True, blank=True, max_length=100)
slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
date_created = models.DateTimeField(blank=True, null=True)
last_updated = models.DateTimeField(blank=True, null=True)

def __str__(self):
        return  '{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email)
 
class Meta:
        verbose_name = _('Profile')


def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            # self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))


        self.slug = slugify('{} {} {} '.format(self.user.first_name, self.user.last_name, self.user.email))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)
        
        
        