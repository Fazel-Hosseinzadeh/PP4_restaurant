from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Table model
class Table(models.Model):

    table_name = models.CharField(
        max_length=50,
        default='Table',
        unique=True
        )
    max_seats = models.PositiveIntegerField(default=4)

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return f"Table  {self.table_name} | Max seats {self.max_seats}"
