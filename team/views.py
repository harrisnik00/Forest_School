from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import TeamMember


class TeamListView(ListView):
    model = TeamMember
    template_name = 'team/list.core'
    context_object_name = 'team_members'

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True, is_featured=True)


class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'team/detail.core'
    context_object_name = 'member'

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True)
