from django.contrib import admin
from django.db import models
from django.contrib import admin
from .models import VolunteerApplication


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "role", "created_at")  # show main fields in admin list
    list_filter = ("role", "created_at")  # filter by role and date
    search_fields = ("name", "email")  # allow searching
    readonly_fields = ("created_at",)  # created_at should not be editable
    ordering = ("-created_at",)  # newest first