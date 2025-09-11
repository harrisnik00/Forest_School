from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")

def services_details(request):
    return render(request, "service-details.html")