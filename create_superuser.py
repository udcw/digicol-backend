# create_superuser.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digicol_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@digicol.com',
        'is_superuser': True,
        'is_staff': True
    }
)

if created:
    user.set_password('DigiCol2026')
    user.save()
    print("✅ Superutilisateur créé !")
else:
    print("⚠️ Le superutilisateur existe déjà.")