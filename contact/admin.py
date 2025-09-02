from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    list_filter = ("submitted_at",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("submitted_at",)
    ordering = ("-submitted_at",)