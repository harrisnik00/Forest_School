"""
URL configuration for forest_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
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
    path('', index, name="index"),           # Changed from 'index/' to ''
    path('about/', about, name="about"),
    path('debug/', debug_view, name='debug'),
]