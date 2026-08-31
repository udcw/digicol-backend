# members/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Member(models.Model):
    """Profil complet du membre DigiCol"""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member_profile'
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    skills = models.TextField(blank=True, help_text="Compétences séparées par des virgules")
    photo = models.ImageField(upload_to='members/photos/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_active_member = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to='members/qrcodes/', blank=True, null=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
    def get_digicol_id(self):
        return self.user.digicol_id
    
    def generate_qr_code(self):
        """Génère un QR Code pour le membre"""
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Utiliser une URL relative au lieu de BASE_URL
            qr_data = f"/verify/{self.user.digicol_id}"
            qr.add_data(qr_data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Sauvegarder l'image
            buffer = BytesIO()
            img.save(buffer, 'PNG')
            filename = f'qr_{self.user.digicol_id}.png'
            self.qr_code.save(filename, File(buffer), save=False)
            return self.qr_code
        except Exception as e:
            print(f"Erreur génération QR: {e}")
            return None
    
    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
        # Ne générer le QR que si l'ID DigiCol existe
        if not self.qr_code and self.user.digicol_id:
            try:
                self.generate_qr_code()
            except:
                pass  # Ignorer les erreurs de QR
        super().save(*args, **kwargs)