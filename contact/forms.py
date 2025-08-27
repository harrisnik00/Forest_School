from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Inquiry, Program


class AdmissionInquiryForm(forms.ModelForm):
    preferred_start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        help_text="When would you like your child to start?"
    )

    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label="Additional Information",
        help_text="Any special needs, dietary requirements, or other information?"
    )

    class Meta:
        model = Inquiry
        fields = [
            'parent_name', 'email', 'phone',
            'child_name', 'child_age',
            'program_interest', 'message'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
            'child_age': forms.NumberInput(attrs={'min': 2, 'max': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program_interest'].queryset = Program.objects.filter(is_active=True)
        self.fields['program_interest'].required = True
        self.fields['child_name'].required = True
        self.fields['child_age'].required = True

        # Set default inquiry type
        self.instance.inquiry_type = 'admission'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('parent_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('program_interest', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('child_name', css_class='form-group col-md-6 mb-3'),
                Column('child_age', css_class='form-group col-md-6 mb-3'),
            ),
            'preferred_start_date',
            'message',
            'additional_info',
            Submit('submit', 'Submit Inquiry', css_class='btn btn-primary btn-lg')
        )
