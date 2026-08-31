#!/bin/bash

echo "🚀 Build du backend DigiCol"

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# ⭐ FORCER LES MIGRATIONS ⭐
echo "🔄 Application des migrations..."
python manage.py makemigrations
python manage.py migrate --noinput

# Créer un superutilisateur
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digicol_backend.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@digicol.com', 'DigiCol2026')
    print('✅ Superutilisateur créé !')
else:
    print('✅ Superutilisateur existe déjà.')
"

echo "✅ Build terminé !"