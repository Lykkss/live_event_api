from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Gestion de Concerts API",
      default_version='v1',
      description="API pour gérer concerts, lieux, organisateurs, catégories, rôles et utilisateurs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/roles/', include('roles.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/lieux/', include('lieux.urls')),
    path('api/organisateurs/', include('organisateurs.urls')),
    path('api/concerts/', include('concerts.urls')),
    # Documentation Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
