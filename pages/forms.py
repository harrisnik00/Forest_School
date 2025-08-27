from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from crispy_forms.bootstrap import FormActions
from contact.models import Inquiry, Program


class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['parent_name', 'email', 'phone', 'child_name', 'child_age',
                  'inquiry_type', 'program_interest', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'child_age': forms.NumberInput(attrs={'min': 1, 'max': 12}),
        }
        labels = {
            'parent_name': 'Your Name',
            'child_name': 'Child\'s Name (if applicable)',
            'child_age': 'Child\'s Age',
            'program_interest': 'Program of Interest',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program_interest'].queryset = Program.objects.filter(is_active=True)
        self.fields['program_interest'].empty_label = "Select a program (optional)"

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('parent_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('inquiry_type', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('child_name', css_class='form-group col-md-6 mb-3'),
                Column('child_age', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            'program_interest',
            'message',
            FormActions(
                Submit('submit', 'Send Message', css_class='btn btn-primary')
            )
        )