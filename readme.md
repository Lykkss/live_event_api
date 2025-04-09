# Live Event API – Backend

Une API REST complète pour gérer des événements (concerts) avec leurs lieux, leurs catégories et leurs organisateurs.

Ce projet est construit sur **Django 5.2** et **Django REST Framework (DRF)** en utilisant le système d’authentification par token (`rest_framework.authtoken`). L’interface d’administration Django sert de back-office pour la gestion des données.

> **Note :** Le projet est utilisé dans un environnement Conda nommé `django`.

---

## Table des Matières

- [Introduction](#introduction)
- [Architecture du Projet](#architecture-du-projet)
- [Schéma Détaillé de la Base de Données](#schéma-détaillé-de-la-base-de-données)
- [Endpoints API et Tests avec curl](#endpoints-api-et-tests-avec-curl)
- [Installation et Déploiement](#installation-et-déploiement)
- [Utilisation de l'Interface d’Administration](#utilisation-de-linterface-dadministration)
- [Notes et Améliorations Futures](#notes-et-améliorations-futures)

---

## Introduction

Ce projet fournit une API pour gérer les concerts ainsi que les entités associées :

- **Organisateur** : Gère les informations sur l’organisateur d’un concert.
- **Lieu** : Contient les informations sur les lieux (salles, stades, etc.) où se déroulent les concerts.
- **Catégorie** : Définit des catégories (ou genres) associées aux concerts (ex. Rock, Pop, Jazz, etc.).
- **Concert** : Représente un concert avec ses détails (titre, description, prix, dates) et référence un Lieu, un Organisateur ainsi qu'une Catégorie.

L’API est sécurisée par authentification Token. Les utilisateurs (par défaut les administrateurs) obtiennent un token via l’endpoint prévu et doivent l’inclure dans l’en-tête des requêtes pour interagir avec l’API.

---

## Architecture du Projet

Le backend est organisé sous la forme d’un projet Django classique, avec une application principale nommée **api**. Voici la structure générale :

live_event_api/ 
├── live_event_api/ # Configuration globale du projet 
│ ├── init.py 
│ ├── asgi.py 
│ ├── settings.py # Paramètres de Django, DRF, BDD, middleware, etc. 
│ ├── urls.py # Routage global (inclut les URLs de l'application) 
│ └── wsgi.py 
├── api/ # Application dédiée aux fonctionnalités de l'API 
│ ├── init.py 
│ ├── admin.py # Enregistrement des modèles dans l'interface d'administration 
│ ├── apps.py 
│ ├── models.py # Modèles : Organisateur, Lieu, Catégorie, Concert 
│ ├── serializers.py # Sérialiseurs pour validation et transformation des données 
│ ├── views.py # ViewSets et endpoints CRUD 
│ ├── urls.py # Routage spécifique à l'API (avec DefaultRouter) 
│ └── migrations/ # Migrations de la base de données 
├── manage.py # Commande de gestion de Django
 └── requirements.txt # Liste des dépendances du projet (optionnel)


**Les principes architecturaux :**

- **Modèles** : Définis dans `models.py`, ils déterminent les entités et leurs relations (clé étrangère).
- **Sérialiseurs** : Situés dans `serializers.py`, ils transforment et valident les données entre les modèles et le format JSON.
- **Views** : Les ViewSets (dans `views.py`) implémentent la logique CRUD et garantissent que seuls des utilisateurs authentifiés peuvent accéder aux endpoints.
- **Routage** : Le fichier `urls.py` (à la fois global et spécifique à l’application) organise les chemins et inclut l’endpoint pour obtenir un token.
- **Interface d’administration** : Permet de gérer manuellement toutes les entités grâce à Django Admin.

---

## Schéma Détaillé de la Base de Données

La base de données contient les tables suivantes :

### 1. Organisateur
- **id** : Clé primaire (entier, auto-incrémenté)
- **name** : Chaîne (max. 100, unique)
- **contact** : Chaîne (max. 100, optionnel)

### 2. Lieu
- **id** : Clé primaire (entier, auto-incrémenté)
- **name** : Chaîne (max. 100)
- **address** : Chaîne (max. 255, optionnel)
- **description** : Texte, optionnel

### 3. Catégorie
- **id** : Clé primaire (entier, auto-incrémenté)
- **name** : Chaîne (max. 100, unique)
- **description** : Texte, optionnel

### 4. Concert
- **id** : Clé primaire (entier, auto-incrémenté)
- **title** : Chaîne (max. 150)
- **description** : Texte
- **price** : Décimal (max_digits=8, decimal_places=2)
- **dateStart** : DateTime (début du concert)
- **dateEnd** : DateTime (fin du concert)
- **lieu_id** : Clé étrangère vers **Lieu** (CASCADE)
- **organisateur_id** : Clé étrangère vers **Organisateur** (CASCADE)
- **categorie_id** : Clé étrangère vers **Catégorie** (CASCADE)

### Représentation Graphique Simplifiée

Organisateur
 ┌────────────┐
 │ id (PK)    │
 │ name       │
 │ contact    │
 └────────────┘
      │
      │ 1-to-many
      ▼
   Concert ─────► Lieu
┌────────────┐    ┌────────────┐
│ id (PK)    │    │ id (PK)    │
│ title      │    │ name       │
│ ...        │    │ address    │
│ dateStart  │    │ description│
│ dateEnd    │    └────────────┘
│ price      │
│ organisateur│
│ categorie │◄──── Catégorie
└────────────┘       ┌────────────┐
                     │ id (PK)    │
                     │ name       │
                     │ description│
                     └────────────┘

Chaque **Concert** est associé à un **Organisateur**, un **Lieu** et une **Catégorie** via des relations ForeignKey (1-à-plusieurs).

---

## Endpoints API et Tests avec curl

L’API est sécurisée par un token. Voici une liste des endpoints principaux avec des exemples de commandes curl pour tester :

### 1. Obtention du Token
**Endpoint :** `/api-token-auth/`  
**Méthode :** POST  
**Paramètres :** `username`, `password`


curl -X POST http://127.0.0.1:8000/api-token-auth/ \
     -d "username=VOTRE_USERNAME&password=VOTRE_MOTDEPASSE"
La réponse sera au format JSON, par exemple :

{"token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

2. Organisateurs
Liste des Organisateurs (GET) :

curl -X GET http://127.0.0.1:8000/api/organisateurs/ \
     -H "Authorization: Token VOTRE_TOKEN"
Création d’un Organisateur (POST) :

curl -X POST http://127.0.0.1:8000/api/organisateurs/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token VOTRE_TOKEN" \
     -d '{"name": "Nouvel Organisateur", "contact": "contact@example.com"}'
3. Lieux
Liste des Lieux (GET) :

curl -X GET http://127.0.0.1:8000/api/lieux/ \
     -H "Authorization: Token VOTRE_TOKEN"
Création d’un Lieu (POST) :

curl -X POST http://127.0.0.1:8000/api/lieux/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token VOTRE_TOKEN" \
     -d '{"name": "Salle de Concert", "address": "123 rue de la Musique", "description": "Lieu idéal"}'

4. Catégories
Liste des Catégories (GET) :

curl -X GET http://127.0.0.1:8000/api/categories/ \
     -H "Authorization: Token VOTRE_TOKEN"

Création d’une Catégorie (POST) :

curl -X POST http://127.0.0.1:8000/api/categories/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token VOTRE_TOKEN" \
     -d '{"name": "Rock", "description": "Concerts de rock"}'
5. Concerts

Liste des Concerts (GET) :

curl -X GET http://127.0.0.1:8000/api/concerts/ \
     -H "Authorization: Token VOTRE_TOKEN"
Création d’un Concert (POST) :

Assurez-vous que les entités référencées existent avant.

curl -X POST http://127.0.0.1:8000/api/concerts/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token VOTRE_TOKEN" \
     -d '{
           "title": "Concert Rock",
           "description": "Un super concert de rock.",
           "price": "150.00",
           "dateStart": "2025-07-13T21:30:00Z",
           "dateEnd": "2025-07-13T23:30:00Z",
           "lieu_id": 1,
           "organisateur_id": 1,
           "categorie_id": 1
       }'
Important : Les requêtes nécessitent l’en-tête d’authentification :
Authorization: Token VOTRE_TOKEN

Installation et Déploiement
Prérequis

Python 3.12 ou supérieur (dans un environnement Conda nommé django)

Django 5.2, Django REST Framework et dépendances (voir requirements.txt)

SQLite pour le développement ou un autre SGBD (PostgreSQL, MySQL) en production

Installation en Environnement de Développement

Cloner le Projet

git clone https://github.com/Lykkss/live_event_api.git
cd live_event_api
Créer et Activer l’Environnement Conda

conda create -n django python=3.12
conda activate django
Installer les Dépendances

pip install -r requirements.txt
Si requirements.txt n'existe pas, installez : django, djangorestframework, djangorestframework-authtoken, django-cors-headers, etc.

Configurer l’Environnement

Modifiez live_event_api/settings.py pour ajuster SECRET_KEY, DEBUG (True en développement) et ALLOWED_HOSTS.

Initialiser la Base de Données (Option B)

Supprimez l'ancienne base si besoin :

rm db.sqlite3
Supprimez les anciens fichiers de migration dans api/migrations/ (sauf __init__.py), puis :

python manage.py makemigrations
python manage.py migrate
Insérer Manuellement la Catégorie par Défaut Lancez le shell et exécutez :

python manage.py shell

Puis dans le shell :

python

from api.models import Categorie
if not Categorie.objects.filter(id=1).exists():
    Categorie.objects.create(id=1, name="Catégorie par défaut", description="Catégorie utilisée par défaut")
exit()
Créer un Superutilisateur

python manage.py createsuperuser
Démarrer le Serveur de Développement

python manage.py runserver
L'interface d'administration est accessible sur http://127.0.0.1:8000/admin/

Testez les endpoints via leurs URL respectives, par exemple : http://127.0.0.1:8000/api/organisateurs/

Déploiement en Production
Configuration

Mettez DEBUG=False et définissez ALLOWED_HOSTS dans settings.py

Stockez les secrets via des variables d’environnement ou un fichier de configuration

Utiliser un Serveur d’Application

Déployez avec Gunicorn ou uWSGI derrière un serveur web (Nginx, Apache)

Exemple avec Gunicorn :

pip install gunicorn
gunicorn live_event_api.wsgi:application --bind 0.0.0.0:8000
Gestion des Fichiers Statiques

python manage.py collectstatic
Configurez votre serveur web pour servir ces fichiers.

Base de Données

Utilisez PostgreSQL, MySQL ou un autre SGBD robuste et configurez settings.py en conséquence.

Sécurité et Monitoring

Mettez en place HTTPS (certificats SSL)

Configurez des backups réguliers et un système de monitoring pour l’application

Utilisation de l'Interface d’Administration
L’interface d’administration Django est accessible via :

localhost:8000/admin/
Connectez-vous avec le compte superutilisateur pour gérer manuellement les enregistrements des modèles (Organisateur, Lieu, Catégorie, Concert).

Notes et Améliorations Futures
Validation des Données : Ajouter des validations supplémentaires (par exemple, vérifier que dateEnd est postérieure à dateStart).

Affinement des Permissions : Adapter les permissions pour restreindre l'accès à certains endpoints selon le rôle de l’utilisateur.

Tests Unitaire et d’Intégration : Mettre en place des tests pour garantir la stabilité de l’API.

Documentation Complète : Utiliser Swagger, Redoc ou drf-yasg pour générer automatiquement la documentation de l’API.

