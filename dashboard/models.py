from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4

import os 

# Create your models here.
class profile(models.Model):
    #Standard Variables
    title = models.CharField(null=True, blank=True, max_length=200)
    #### ADD OTHER VARIABLES HERE
    
    
    #Related Variables
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}{}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{}{}'.format(self.title, self.uniqueId))


        self.slug = slugify('{}{}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(profile, self).save(*args, **kwargs)