from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Organisateur
from .serializers import OrganisateurSerializer

class OrganisateurViewSet(viewsets.ModelViewSet):
    queryset = Organisateur.objects.all()
    serializer_class = OrganisateurSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
