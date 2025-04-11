# api/models.py

from django.db import models

class Organisateur(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Lieu(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Concert(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField()
    lieu_id = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='concerts')
    organisateur_id = models.ForeignKey(Organisateur, on_delete=models.CASCADE, related_name='concerts')
    # Autoriser temporairement des valeurs NULL pour le champ categorie
    categorie_id = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='concerts',
        null=True,       # autorise la valeur null
        blank=True       # permet un formulaire vide
    )

    def __str__(self):
        return self.title
