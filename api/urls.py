# api/urls.py
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import OrganisateurViewSet, LieuViewSet, ConcertViewSet, CategorieViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'organisateurs', OrganisateurViewSet)
router.register(r'lieux', LieuViewSet)
router.register(r'concerts', ConcertViewSet)
router.register(r'categories', CategorieViewSet) 

urlpatterns = [
    path('', lambda request: HttpResponse("Bienvenue sur l'API de Live Event!"), name='home'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
