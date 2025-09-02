from django.urls import path
from .views import CareersView

app_name = 'careers'

urlpatterns = [
    path('', CareersView, name='careers-view'),
]