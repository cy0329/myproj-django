from django.contrib import admin

from maple.models import Character


@admin.register(Character)
class CharaterAdmin(admin.ModelAdmin):
    list_display = ["id", "job"]
    list_display_links = ["job"]

