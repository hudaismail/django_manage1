from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True, null=True)
    bio1 = models.TextField(blank=True, null=True)
    bio2 = models.TextField(blank=True, null=True)
    bio3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name

