import os
import random
from django.db import models
from django.contrib.auth.models import AbstractUser

def profile_name(instance, filename):
    # This function is to generate random names for each profile image.
    return f'{instance.username}-{"".join([str(random.randint(0, 9)) for _ in range(8)])}.{os.path.splitext(filename)[1]}'

class User(AbstractUser):
    name = models.CharField(max_length=120, verbose_name='FullName')
    profile = models.ImageField(upload_to=profile_name, default='Default.png',)

    REQUIRED_FIELDS = ['name']

class Ticket(models.Model):
    name = models.CharField(max_length=120, verbose_name='FullName')
    email = models.EmailField()
    message = models.TextField(max_length=620)
    date = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.message[:80]
