from django.contrib import admin
from .models import Camp

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "week_price", "is_active")
    list_filter = ("is_active", "sleepover_option", "start_date")
    search_fields = ("name", "description")
    ordering = ("-start_date",)
    readonly_fields = ("created_at", "updated_at")