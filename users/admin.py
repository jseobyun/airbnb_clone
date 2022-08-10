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


# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
#     """
#     CustomUserAdmin
#     """

# list_display = ("username", "email", "gender", "language", "currency", "superhost")
# list_filter = ("superhost", "language", "currency")
