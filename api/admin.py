# api/admin.py
from django.contrib import admin
from .models import Organisateur, Lieu, Concert, Categorie

admin.site.register(Organisateur)
admin.site.register(Lieu)
admin.site.register(Concert)
admin.site.register(Categorie)
