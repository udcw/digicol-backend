# digicol_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def health_check(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'DigiCol API is running',
        'version': '1.0.0'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check),
    
    # Auth
    path('api/auth/', include('accounts.urls')),
    
    # Members
    path('api/members/', include('members.urls')),
    
    # Courses
    path('api/courses/', include('courses.urls')),
    
    # Projects ⭐ AJOUTER CETTE LIGNE
    path('api/projects/', include('projects.urls')),
    
    # Certificates
    path('api/certificates/', include('certificates.urls')),
    
    # Blog
    path('api/blog/', include('blog.urls')),
    
    # Events
    path('api/events/', include('events.urls')),
    
    # Community
    path('api/community/', include('community.urls')),
    
    # Notifications
    path('api/notifications/', include('notifications.urls')),
    
    # Payments
    path('api/payments/', include('payments.urls')),
    
    # Opportunities
    path('api/opportunities/', include('opportunities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)