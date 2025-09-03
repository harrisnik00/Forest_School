from django.urls import path
from .views import CareersView

app_name = 'volunteer'

urlpatterns = [
    path('', CareersView, name='volunteer-view'),
]