# api/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organisateur, Lieu, Concert, Categorie
from .serializers import OrganisateurSerializer, LieuSerializer, ConcertSerializer, CategorieSerializer

class OrganisateurViewSet(viewsets.ModelViewSet):
    queryset = Organisateur.objects.all()
    serializer_class = OrganisateurSerializer
    permission_classes = [IsAuthenticated]

class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticated]

class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    permission_classes = [IsAuthenticated]

# Nouveau ViewSet pour Categorie
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAuthenticated]
