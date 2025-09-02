from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page, TeamMember, FAQ, AcademicCalendar


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display= ("title", "slug")
    search_fields = ("title","slug")
    prepopulated_fields = {"slug":("title",)}

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display= ("name", "role")
    search_fields = ("name", "role")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display= ("question", )
    search_fields = ("question", "answer")
