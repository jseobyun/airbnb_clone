from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "baths",
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # for hide and show
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    # for ordering item by below attr
    # ordering = (
    #     "name",
    #     "price",
    #     "bedrooms",
    # )
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "house_rules",
        "city",
        "country",
    )
    # ^ denotes startswith
    # default denotes icontains
    # foreign_key__attr access to host.username
    search_fields = ("^city", "^host__username")

    # only for many-to-many
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # obj is a current row
    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Num# amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
