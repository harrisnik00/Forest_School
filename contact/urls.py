from django.urls import path
from .views import ContactForm

app_name = 'contact'

urlpatterns = [
   path('',"Contact-Form/", ContactForm, name="contact-form" ),

]