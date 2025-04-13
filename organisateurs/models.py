from django.db import models

class Organisateur(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
