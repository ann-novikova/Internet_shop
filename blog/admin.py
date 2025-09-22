from django.contrib import admin

from .models import Article


@admin.register(Article)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "is_published", "views_count")
    list_filter = ("title",)
    search_fields = ("title",)
