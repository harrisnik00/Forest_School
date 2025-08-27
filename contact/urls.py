from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.AdmissionsView.as_view(), name='programs'),
    path('inquiry/', views.AdmissionInquiryView.as_view(), name='inquiry'),
    path('inquiry/success/', views.TemplateView.as_view(
        template_name='admissions/inquiry_success.core'
    ), name='inquiry_success'),
]