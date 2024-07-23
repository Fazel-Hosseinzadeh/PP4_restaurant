from django.contrib import admin
from .models import Table, Booking
from rangefilter.filters import DateRangeFilter

# Register Table model
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Lists table name and maximum seats for display in admin.
    """
    list_display = ( 'table_name', 'max_seats')
    
    
# Register Book model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Lists booking details for display in admin, provides search fields, 
    and filters by requested date, guest count, status, and requested time.
    """
    list_display = (
        'user',
        'name',
        'phone',
        'email',
        'guest_count',
        'status',
        'table',
        'requested_date',
        'requested_time',
        )

    search_fields = [
                    'name',
                    'email',
                    'phone',
                     
                     ]
    list_filter = (('requested_date', DateRangeFilter),
                    'guest_count',
                    'status',
                    'requested_time',
                   )
    actions = ['confirm_bookings']


    def confirm_bookings(self, request, queryset):
        """
        Custom action to confirm selected bookings.
        """
        queryset.update(status='Booking Confirmed')