
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import traceback

def debug_view(request):
    try:
        return HttpResponse("<h1>Debug Test</h1><p>Django is working!</p>")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}<br><pre>{traceback.format_exc()}</pre>")

def index(request):
    return HttpResponse("<h1>Home Page</h1><p>Welcome to Forest School!</p>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>Learn about our forest school!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # home / about / etc.
    path('camps/', include('programs.urls')),
    path('team/', include('team.urls')),
    path('news/', include('news.urls')),
    path('volunteers/', include('volunteers.urls')),
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =============================================================================
# CORE APP URLs (core/urls.py)