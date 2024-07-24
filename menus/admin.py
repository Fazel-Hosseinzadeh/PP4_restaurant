from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import FoodItem, DrinkItem


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing food items.

    Displays fields for food items in the admin list view and provides search
    and filter options.
    Includes a rich-text editor for the `description` field using Summernote.

    **Fields**
    ``list_display``
        Fields to display in the admin list view: `food_name`, `food_type`,
        `price`, and `available`.
    ``search_fields``
        Fields that can be searched: `food_name` and `description`.
    ``list_filter``
        Filters available in the admin list view: `available` and `food_type`.
    ``summernote_fields``
        Specifies the fields to be rendered with the Summernote rich-text
        editor: `description`.

    **Template**
    None
    """

    list_display = (
        "food_name",
        "food_type",
        "price",
        "available",
    )
    search_fields = ("food_name", "description")
    list_filter = ("available", "food_type")
    summernote_fields = ("description",)


@admin.register(DrinkItem)
class DrinkAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing drink items.

    Displays fields for drink items in the admin list view and provides search
    and filter options.
    Includes a rich-text editor for the `description` field using Summernote.

    **Fields**
    ``list_display``
        Fields to display in the admin list view: `drink_name`, `drink_type`,
        `price`, and `available`.
    ``search_fields``
        Fields that can be searched: `drink_name` and `description`.
    ``list_filter``
        Filters available in the admin list view: `available` and `drink_type`.
    ``summernote_fields``
        Specifies the fields to be rendered with the Summernote rich-text
        editor:`description`.

    **Template**
    None
    """

    list_display = (
        "drink_name",
        "drink_type",
        "price",
        "available",
    )
    search_fields = ("drink_name", "description")
    list_filter = ("available", "drink_type")
    summernote_fields = ("description",)
