from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Camp


class CampListView(ListView):
    model = Camp
    template_name = 'camps/list.core'
    context_object_name = 'camps'

    def get_queryset(self):
        return Camp.objects.filter(
            is_open_for_registration=True,
            end_date__gte=timezone.now().date()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_camps'] = self.get_queryset()
        context['past_camps'] = Camp.objects.filter(
            end_date__lt=timezone.now().date()
        )[:6]  # Show some past camps for reference
        return context


class CampDetailView(DetailView):
    model = Camp
    template_name = 'camps/detail.core'
    context_object_name = 'camp'