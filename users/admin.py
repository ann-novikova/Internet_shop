from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )
    list_filter = ("email",)
    search_fields = ("email",)

