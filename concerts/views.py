from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils import timezone
from .models import Concert
from .serializers import ConcertSerializer
from .permissions import IsAdminOrOwnerOrReadOnly
from rest_framework.exceptions import ValidationError

class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Vérification de la date de début
        if serializer.validated_data['DateStart'] < timezone.now():
            raise ValidationError({"code": "ERR_DATE_PASSEE", "message": "La date de début ne peut pas être dans le passé."})
        serializer.save()
