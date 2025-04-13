from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganisateurViewSet

router = DefaultRouter()
router.register(r'', OrganisateurViewSet, basename='organisateurs')

urlpatterns = [
    path('', include(router.urls)),
]
