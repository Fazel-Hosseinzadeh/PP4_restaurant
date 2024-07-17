from django.contrib import admin
from .models import Table, Booking
from rangefilter.filters import DateRangeFilter

# Register Table model
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ( 'table_name', 'max_seats')
    
    
# Register Book model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
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

    # Add actions to do on the bookings
    def confirm_bookings(self, request, queryset):
        queryset.update(status='Booking Confirmed')