from django.contrib import admin
from .models import ContactMessage, ContactContent
from django_summernote.admin import SummernoteModelAdmin

# Admin Contact Content
@admin.register(ContactContent)
class ContactContentAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


# Admin Contact Message
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'read',
        )

    search_fields = [
                    'name',
                    'email',
                     ]
    list_filter = (
                    'read',
                   )
    actions = ['read']

    # Add actions to do on the bookings
    def read(self, request, queryset):
        queryset.update(read=True)
    