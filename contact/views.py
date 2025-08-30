
from django.shortcuts import render, redirect
def ContactForm(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_thankyou")

    else:
        form = ContactForm()
        return render(request, "index.html", {"form": form})