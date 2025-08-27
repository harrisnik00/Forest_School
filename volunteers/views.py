from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import VolunteerApplication


class CareersView(ListView):
    model = VolunteerApplication
    template_name = 'careers/list.html'
    context_object_name = 'job_openings'

    def get_queryset(self):
        return VolunteerApplication.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urgent_jobs'] = self.get_queryset().filter(is_urgent=True)
        context['regular_jobs'] = self.get_queryset().filter(is_urgent=False)
        return context


class JobDetailView(DetailView):
    model = VolunteerApplication
    template_name = 'careers/detail.html'
    context_object_name = 'job'

    def get_queryset(self):
        return VolunteerApplication.objects.filter(is_active=True)
