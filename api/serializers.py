# api/serializers.py
from rest_framework import serializers
from .models import Organisateur, Lieu, Concert, Categorie

class OrganisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisateur
        fields = '__all__'

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'

# Nouveau serializer pour Categorie
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ConcertSerializer(serializers.ModelSerializer):
    # Pour l'affichage détaillé en lecture
    lieu = LieuSerializer(read_only=True)
    organisateur = OrganisateurSerializer(read_only=True)
    categorie = CategorieSerializer(read_only=True)
    # Pour la création/mise à jour, on attend les identifiants (FK)
    lieu_id = serializers.PrimaryKeyRelatedField(queryset=Lieu.objects.all(), source='lieu')
    organisateur_id = serializers.PrimaryKeyRelatedField(queryset=Organisateur.objects.all(), source='organisateur')
    categorie_id = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all(), source='categorie')

    class Meta:
        model = Concert
        fields = [
            'id',
            'title',
            'description',
            'price',
            'dateStart',
            'dateEnd',
            'lieu_id', 'organisateur_id', 'categorie_id',
        ]
        read_only_fields = ['id', 'lieu_id', 'organisateur_id', 'categorie_id']
