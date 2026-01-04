# Utilise l'image officielle Python avec uv pré-installé
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Définit le répertoire de travail
WORKDIR /app

# Variables d'environnement pour Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_SYSTEM_PYTHON=1

# Copie les fichiers de dépendances
COPY pyproject.toml uv.lock ./

# Installe les dépendances avec uv
RUN uv sync --frozen --no-dev

# Copie le code source
COPY . .

# Collecte les fichiers statiques
RUN uv run python manage.py collectstatic --noinput || true

# Expose le port 8000
EXPOSE 8000

# Commande par défaut pour lancer le serveur
CMD ["uv", "run", "gunicorn", "mspr2_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
