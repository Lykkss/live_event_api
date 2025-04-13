from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Exemple : 'admin', 'organisateur', 'standard'

    def __str__(self):
        return self.name
