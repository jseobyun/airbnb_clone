from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# this class exists for managing generated Users


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """
    CustomUserAdmin
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "birthdata",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )


# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
#     """
#     CustomUserAdmin
#     """

# list_display = ("username", "email", "gender", "language", "currency", "superhost")
# list_filter = ("superhost", "language", "currency")
