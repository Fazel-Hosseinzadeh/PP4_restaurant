from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin view for managing Post instances.
    """

    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = (
        "status",
        "created_on",
    )
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Admin view for managing Comment instances.
    """

    list_filter = ("author", "approved")
    list_display = ("author", "approved", "created_on", "body")
    actions = ["confirm_comments", "unconfirmed_commet"]

    def confirm_comments(self, request, queryset):
        """
        Mark selected comments as approved.
        """
        queryset.update(approved=True)

    def unconfirmed_commet(self, request, queryset):
        """
        Mark selected comments as unapproved.
        """
        queryset.update(approved=False)
