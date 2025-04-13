# users/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from roles.models import Role

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Affecte un rôle par défaut si besoin (exemple : rôle "standard")
        default_role = Role.objects.filter(name='standard').first()
        UserProfile.objects.create(user=instance, role=default_role)
    else:
        instance.profile.save()
