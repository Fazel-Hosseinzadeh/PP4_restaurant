from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Table(models.Model):
    """
    Stores a single table entry.
    """
    table_name = models.CharField(
        max_length=50,
        default='Table',
        unique=True
        )
    max_seats = models.PositiveIntegerField(default=4)

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return f"{self.table_name} | Max seats {self.max_seats}"
    

# Restaurants time slots 
time_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
)


# Booking Status
status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)

# booking model
class Booking(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User` and :model:`Table`.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='Awaiting confirmation'
        )
    seats = (
        (1, "1 Guest"),
        (2, "2 Guests"),
        (3, "3 Guests"),
        (4, "4 Guests"),
        (5, "5 Guests"),
        (6, "6 Guests"),
        )
    guest_count = models.PositiveIntegerField(choices=seats, default=4)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25,
        choices=time_slots,
        default='13:00'
        )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_reserved",
        null=True
        )

    class Meta:
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'table')

    def __str__(self):
        return f"name {self.name} | guest Nr:{self.guest_count} | on {self.requested_date} | {self.status}"
