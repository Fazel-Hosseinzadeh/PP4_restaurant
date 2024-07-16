from django import forms
from .models import Booking
from datetime import datetime
from django.forms.widgets import DateInput


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'guest_count',
            'table',
            'requested_date',
            'requested_time',
            )
        
        labels = {
            
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
            'guest_count': 'Guest Number',
            'table' : 'Table',
            'requested_date' : 'Requested Day',
            'requested_time' : 'Requested Time',
        }
        
        widgets = {
            
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'phone': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'guest_count': forms.Select(attrs={'class' : 'form-control'}),
            'table' : forms.Select(attrs={'class' : 'form-control'}),
            'requested_date' : forms.widgets.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'min ': '2024-07-16', ' max': '2050-01-01'}),
            'requested_time' : forms.Select(attrs={'class' : 'form-control'}),
            }
        