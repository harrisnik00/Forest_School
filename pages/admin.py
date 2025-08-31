from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page, TeamMember, FAQ, AcademicCalendar

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published", "updated_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    ordering = ("order",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    ordering = ("order",)


@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ("year", "published", "created_at")

