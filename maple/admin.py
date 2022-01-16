from django.contrib import admin

from maple.models import Character, Category


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["id", "job"]
    list_display_links = ["job"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]