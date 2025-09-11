from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home , name="index"),
    path("portfolio-details/", views.portfolio_details, name="portfolio_details"),
    path("service-details/", views.services_details, name="services_details"),
    path("camps/", views.camps, name="camps"),
]

