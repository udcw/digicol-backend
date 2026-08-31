# members/views.py

from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer

class MemberProfileView(generics.RetrieveUpdateAPIView):
    """Profil du membre connecté - Création automatique si inexistant"""
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        user = self.request.user
        try:
            return user.member_profile
        except Member.DoesNotExist:
            # Créer automatiquement un membre si inexistant
            member = Member.objects.create(
                user=user,
                full_name=user.get_full_name() or user.username,
                phone='',
                city='',
                study_level='',
                domain='',
                skills='',
                bio='',
                is_active_member=True
            )
            return member

class MemberDetailView(generics.RetrieveAPIView):
    """Détail public d'un membre"""
    queryset = Member.objects.filter(is_active_member=True)
    serializer_class = MemberSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'user__digicol_id'
    lookup_url_kwarg = 'digicol_id'
    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Member.DoesNotExist:
            return Response(
                {'detail': 'Membre non trouvé.'},
                status=status.HTTP_404_NOT_FOUND
            )