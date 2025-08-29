from django.contrib import admin
from django.db import models

from django.contrib import admin
from .models import VolunteerApplication


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "volunteer_type", "submitted_at")
    list_filter = ("volunteer_type", "submitted_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("submitted_at",)

    # Optional: order by newest applications first
    ordering = ("-submitted_at",)