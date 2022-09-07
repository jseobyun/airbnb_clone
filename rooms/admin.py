from curses import raw
from django.contrib import admin
from django.utils.html import mark_safe
from . import models


# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)
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
                    "bedrooms",
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
        "count_photos",
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

    raw_id_fields = ("host",)

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

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Num# photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    list_display = ("__str__", "get__thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
