from django.db import models
import uuid
from django.core.validators import FileExtensionValidator, URLValidator
import os
import random
def icon_name(instance, filename):
    # This function is to generate random names for each icon.
    return f'icons/{instance.title}-{"".join([str(random.randint(0, 9)) for _ in range(8)])}.{os.path.splitext(filename)[1]}'

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('#d43428', 'Red'),
        ('#2853d4', 'Blue'),
        ('#d4a028', 'Yellow'),
        ('#a028d4', 'Purple')
    ]

    title = models.CharField(max_length=60)
    icon = models.CharField(max_length=80, verbose_name='Name of icon in google')
    color = models.CharField(choices=CATEGORY_CHOICES, max_length=8)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(blank=False)
    short_desc = models.TextField(max_length=100, blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_notes')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_of')
    public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

