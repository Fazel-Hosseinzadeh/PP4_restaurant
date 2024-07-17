from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register Post model
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register Comment model
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_filter = (
    'author',
    'approved'
    )
    list_display = (
    'author',
    'approved',
    'created_on',
    'body'
    )
    actions = ['confirm_comments', 'unconfirmed_commet']
    
    # Add actions to do on the bookings
    def confirm_comments(self, request, queryset):
        queryset.update(approved= True)
    
    def unconfirmed_commet(self, request, queryset):
        queryset.update(approved= False)