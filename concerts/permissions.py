from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Lecture autorisée
        if request.method in SAFE_METHODS:
            return True
        # Vérification si l'utilisateur est admin
        if request.user.is_staff:
            return True
        # Vérification pour les organisateurs
        try:
            if request.user.profile.role.name == 'organisateur':
                # Supposons qu’un utilisateur organisateur possède un lien vers un objet Organisateur
                return obj.organisateur.id == request.user.profile.organisateur.id
        except AttributeError:
            pass
        return False
