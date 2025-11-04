from django.contrib import admin

from .models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ("name", "milk_type", "origin", "price", "is_vegan")
    list_filter = ("milk_type", "is_vegan")

    prepopulated_fields = {"slug": ("name",)}

    search_fields = ("name", "origin")
    ordering = ("name",)
