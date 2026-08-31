# members/urls.py

from django.urls import path
from .views import MemberProfileView, MemberDetailView

urlpatterns = [
    path('profile/', MemberProfileView.as_view(), name='member-profile'),
    path('verify/<str:digicol_id>/', MemberDetailView.as_view(), name='member-verify'),
]