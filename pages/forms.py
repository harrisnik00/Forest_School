
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages

def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['contact@example.com'],  # replace with your email
                fail_silently=False,
            )
            messages.success(request, "Thank you! Your message has been sent.")
    return redirect('core:index')