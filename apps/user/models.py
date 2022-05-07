from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField()
    nickname = models.CharField(max_length=12)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}--{self.first_name}"
