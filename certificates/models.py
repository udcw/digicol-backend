# certificates/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class Certificate(models.Model):
    """Certificat DigiCol"""
    
    certificate_id = models.CharField(max_length=50, unique=True, editable=False)
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='certificates')
    enrollment = models.OneToOneField(
        'courses.Enrollment',
        on_delete=models.CASCADE,
        related_name='certificate'
    )
    issue_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='certificates/pdfs/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='certificates/qrcodes/', blank=True, null=True)
    is_verified = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.certificate_id:
            year = timezone.now().year
            count = Certificate.objects.filter(certificate_id__startswith=f'CERT-{year}').count() + 1
            self.certificate_id = f'CERT-{year}-{count:04d}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.certificate_id} - {self.member.full_name}"