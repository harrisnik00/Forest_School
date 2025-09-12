from django.shortcuts import render
from .models import Team

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")

def services_details(request):
    return render(request, "service-details.html")

def camps(request):
    return render(request, "camps.html")

def index(request):
    team = Team.objects.all()
    return render(request, "index.html", {"team": team})