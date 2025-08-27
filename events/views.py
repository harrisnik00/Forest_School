from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Event
import calendar


class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(
            is_published=True,
            is_cancelled=False,
            start_datetime__gte=timezone.now()
        )


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        return Event.objects.filter(is_published=True)