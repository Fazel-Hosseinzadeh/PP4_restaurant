from django.contrib import admin
from .models import Table, Booking

# Register Table model
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ( 'table_name', 'max_seats')