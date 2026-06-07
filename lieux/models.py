from django.db import models

class Lieu(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField()
    toilettes = models.BooleanField(default=False)
    buvettes = models.BooleanField(default=False)

    def __str__(self):
        return self.name
