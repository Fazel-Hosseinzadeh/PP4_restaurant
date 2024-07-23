from django.contrib import admin
from .models import ContactMessage, ContactContent
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactContent)
class ContactContentAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing ContactContent.

    Provides a rich-text editor for the `content` field using Summernote. This admin class allows users to
    edit the content with enhanced text formatting options.

    **Fields**
    ``summernote_fields``
        Specifies the fields to be rendered with the Summernote rich-text editor.

    **Template**
    None
    """

    summernote_fields = ("content",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing ContactMessage instances.

    Displays key fields in the admin list view, provides search functionality, and allows filtering by
    the read status. Includes a custom action to mark messages as read.

    **Fields**
    ``list_display``
        Fields to display in the admin list view: `name`, `email`, and `read`.
    ``search_fields``
        Fields that can be searched: `name` and `email`.
    ``list_filter``
        Filters available in the admin list view: `read`.

    **Actions**
    ``read``
        Custom action to mark selected messages as read.

    **Template**
    None
    """

    list_display = (
        "name",
        "email",
        "read",
    )

    search_fields = [
        "name",
        "email",
    ]
    list_filter = ("read",)
    actions = ["read"]

    def read(self, request, queryset):
        """
        Marks selected messages as read.

        Updates the `read` field to `True` for the selected `ContactMessage` instances.
        """
        queryset.update(read=True)
