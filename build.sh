#!/bin/bash

echo "🚀 Build du backend DigiCol"

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Appliquer les migrations
python manage.py migrate

echo "✅ Build terminé !"