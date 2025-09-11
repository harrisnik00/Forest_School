
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from volunteer.views import CareersView
from . import views

import traceback



urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact/", include("contact.urls", namespace="contact")),
    path("", include("pages.urls", namespace="pages")),
    path("camps/", include("camps.urls", namespace="camps")),

    path("", views.home, name="home"),
    path("", include("volunteer.urls")),
    path("", include("camps.urls")),
    path("volunteer/", include("volunteer.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =============================================================================
# CORE APP URLs (core/urls.py)