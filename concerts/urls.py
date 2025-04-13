from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConcertViewSet

router = DefaultRouter()
router.register(r'', ConcertViewSet, basename='concerts')

urlpatterns = [
    path('', include(router.urls)),
]
