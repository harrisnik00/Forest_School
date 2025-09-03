from django import forms
from .models import VolunteerApplication

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['name', 'email', 'message']
        widgets = {"role": forms.RadioSelect()}