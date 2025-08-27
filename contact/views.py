from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Program, PricingOption
from .forms import AdmissionInquiryForm


class AdmissionsView(TemplateView):
    template_name = 'admissions/admissions.core'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'morning_programs': Program.objects.filter(
                program_type='morning',
                is_active=True
            ).prefetch_related('pricing_options'),
            'other_programs': Program.objects.filter(
                program_type__in=['afternoon', 'weekend'],
                is_active=True
            ),
        })
        return context


class AdmissionInquiryView(CreateView):
    form_class = AdmissionInquiryForm
    template_name = 'admissions/inquiry.core'
    success_url = reverse_lazy('admissions:inquiry_success')

    def form_valid(self, form):
        messages.success(
            self.request,
            'Thank you for your admission inquiry! We will contact you within 24 hours.'
        )
        return super().form_valid(form)