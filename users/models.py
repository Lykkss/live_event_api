# users/models.py

from django.db import models
from django.contrib.auth.models import User
from roles.models import Role

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
