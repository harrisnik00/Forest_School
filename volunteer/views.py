from django.shortcuts import render, redirect
from .forms import VolunteerApplicationForm

def CareersView(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_thankyou")
    else:
        form = VolunteerApplicationForm()

    return render(request, "volunteerapplication.html", {"form": form})

