# members/views.py

from rest_framework import generics, permissions
from .models import Member
from .serializers import MemberSerializer
from rest_framework.permissions import IsAuthenticated

class MemberProfileView(generics.RetrieveUpdateAPIView):
    """Profil du membre connecté - Création automatique si inexistant"""
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        user = self.request.user
        # Création automatique si le Member n'existe pas
        member, created = Member.objects.get_or_create(
            user=user,
            defaults={
                'full_name': f"{user.first_name} {user.last_name}".strip() or user.username,
                'phone': user.phone or '',
                'city': '',
                'study_level': '',
                'domain': '',
                'skills': '',
                'is_active_member': True
            }
        )
        if created:
            print(f"Member cree automatiquement pour {user.username}")
        return member

class MemberDetailView(generics.RetrieveAPIView):
    """Détail public d'un membre"""
    queryset = Member.objects.filter(is_active_member=True)
    serializer_class = MemberSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'user__digicol_id'
    lookup_url_kwarg = 'digicol_id'