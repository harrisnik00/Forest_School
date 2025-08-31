from django.urls import path
from . import views

app_name = 'pages'

from django.urls import path
from .views import contact_submit

urlpatterns = [
path("<slug:slug>/", views.page_detail, name="page_detail"),   # For generic pages
    path("team/", views.team_list, name="team_list"),              # Team page
    path("faq/", views.faq_list, name="faq_list"),                 # FAQ page
    path("calendar/", views.calendar_list, name="calendar_list"),  ]