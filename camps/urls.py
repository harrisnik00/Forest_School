from django.urls import path
from . import views

app_name = 'camps'

urlpatterns = [
    path("", views.camp_list, name="camp_list"),
    path("<int:pk>/", views.camp_detail, name="camp_detail"),
    path("", views.index, name="index"),
]