# users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    
    def ready(self):
        import users.signals  # Permet d'enregistrer les signaux
