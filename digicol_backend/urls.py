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

# digicol_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        'status': 'ok',
        'message': 'DigiCol API is running',
        'version': '1.0.0'
    })

urlpatterns = [
    path('admin/', admin.site.urls),  # ⭐ RÉACTIVER
    path('api/health/', health_check),
    path('api/auth/', include('accounts.urls')),
    path('api/members/', include('members.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/certificates/', include('certificates.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/events/', include('events.urls')),
    path('api/community/', include('community.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/opportunities/', include('opportunities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)