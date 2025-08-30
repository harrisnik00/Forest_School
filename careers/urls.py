from django.urls import path
from .views import CareersView

app_name = 'careers'

urlpatterns = [
    path ('',"Careers-view/", CareersView, name='careers-view' ),
]