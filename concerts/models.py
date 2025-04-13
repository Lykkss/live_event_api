from django.db import models
from django.utils import timezone
from lieux.models import Lieu
from organisateurs.models import Organisateur
from categories.models import Categorie

class Concert(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    DateStart = models.DateTimeField()
    DateEnd = models.DateTimeField()
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    organisateur = models.ForeignKey(Organisateur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title', 'DateStart', 'lieu', 'organisateur', 'categorie')

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.DateStart < timezone.now():
            raise ValidationError("La date de début ne peut pas être dans le passé.")

    def __str__(self):
        return self.title
