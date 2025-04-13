from django.db import models

class Lieu(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
