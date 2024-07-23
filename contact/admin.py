from django.contrib import admin
from .models import ContactContent
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactContent)
class ContactContentAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
