from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import SiteSettings, HomePage
from .forms import ContactForm
from news.models import NewsPost
from events.models import Event
from programs.models import Camp
from django.utils import timezone


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'site_settings': SiteSettings.objects.first(),
            'home_content': HomePage.objects.filter(is_active=True).first(),
            'featured_news': NewsPost.objects.filter(is_published=True, is_featured=True)[:3],
            'upcoming_events': Event.objects.filter(
                start_datetime__gte=timezone.now(),
                is_published=True,
                is_cancelled=False
            )[:2],
            'featured_camps': Camp.objects.filter(is_featured=True, is_open_for_registration=True)[:2],
        })
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'site_settings': SiteSettings.objects.first(),
            'form': ContactForm(),
        })
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save inquiry
            form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f"New Contact Form Submission - {form.cleaned_data['inquiry_type']}",
                    message=f"""
                    New contact form submission:

                    Name: {form.cleaned_data['parent_name']}
                    Email: {form.cleaned_data['email']}
                    Phone: {form.cleaned_data['phone']}
                    Type: {form.cleaned_data['inquiry_type']}

                    Message:
                    {form.cleaned_data['message']}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except:
                pass  # Email sending failed but form was saved

            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('core:contact')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)