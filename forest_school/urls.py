
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import traceback



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Careers-view', include('careers.urls')),
    path('Contac-Form/', include('contact.urls')),
path("", include("pages.urls", namespace="pages")),
path("camps/", include("camps.urls", namespace="camps")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =============================================================================
# CORE APP URLs (core/urls.py)