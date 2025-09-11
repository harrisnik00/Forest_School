from django.urls import path
from .views import CareersView
from . import views
app_name = 'volunteer'

urlpatterns = [
    path("careers/", views.CareersView, name="careers"),
]