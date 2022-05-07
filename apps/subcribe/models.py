from django.db import models
from apps.user.models import User



class Subscribe(models.Model):
    user = models.ManyToManyField(
        User, 
        related_name='user_to_subscribe')

    def __str__(self):
        return f"{self.user.username}"
