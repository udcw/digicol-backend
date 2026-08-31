#!/bin/bash

echo "🚀 Build du backend DigiCol"

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur (tout en une ligne)
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digicol_backend.settings'); import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); user, created = User.objects.get_or_create(username='admin', defaults={'email':'admin@digicol.com', 'is_superuser':True, 'is_staff':True}); user.set_password('DigiCol2026'); user.save(); print('✅ Admin créé' if created else '✅ Admin existe déjà')"

echo "✅ Build terminé !"