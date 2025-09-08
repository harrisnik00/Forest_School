from django.http import HttpResponse
import traceback

from django.shortcuts import render

def home(request):
    return render(request, "index.html")
