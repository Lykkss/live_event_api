from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Lieu
from .serializers import LieuSerializer

class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
