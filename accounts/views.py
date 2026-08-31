# accounts/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """Inscription d'un nouvel utilisateur"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'success': True,
                'message': 'Inscription réussie',
                'user': UserSerializer(user).data
            }, status=201)
        return Response(serializer.errors, status=400)
class AdminLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('admin:index')
    
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
class CustomTokenObtainPairView(TokenObtainPairView):
    """Connexion - Obtention du token JWT"""
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """Profil utilisateur"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user