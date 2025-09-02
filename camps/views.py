

from django.shortcuts import render, get_object_or_404
from .models import Camp

def camp_list(request):
    camps = Camp.objects.filter(is_active=True).order_by("order", "start_date")
    return render(request, "camps/camp_list.html", {"camps": camps})

def camp_detail(request, pk):
    camp = get_object_or_404(Camp, pk=pk, is_active=True)
    return render(request, "camps/camp_detail.html", {"camp": camp})