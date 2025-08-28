from django.urls import path
from . import views

app_name = 'pages'

from django.urls import path
from .views import contact_submit

urlpatterns += [
    path("contact-submit/", contact_submit, name="contact_submit"),
]