from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser): #this model contains all the fields of the default User model: username, first, last_name, email etc
    age = models.PositiveIntegerField(null = True, blank = True) #and additional age field