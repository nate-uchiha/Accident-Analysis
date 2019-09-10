from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length = 256,unique=True,blank=True)
    password = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length = 256,editable=True,blank=True)
    last_name = models.CharField(max_length = 256,editable=True,blank=True)
    avatar = models.ImageField(upload_to='images/', editable=True,blank=True)

    def __str__(self):
        return self.first_name
