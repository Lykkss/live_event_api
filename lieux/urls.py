from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LieuViewSet

router = DefaultRouter()
router.register(r'', LieuViewSet, basename='lieux')

urlpatterns = [
    path('', include(router.urls)),
]
