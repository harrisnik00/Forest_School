from django.urls import path
from . import views  # import the views module

app_name = 'camps'

urlpatterns = [
    path("", views.camp_list, name="camp_list"),
    path("<int:pk>/", views.camp_detail, name="camp_detail"),
]