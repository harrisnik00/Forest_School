from django import forms
from .models import Contact

class ContactForm(forms.form):
    model= Contact
    fields= ["name", "email", "message"]