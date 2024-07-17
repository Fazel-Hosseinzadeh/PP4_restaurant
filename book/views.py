from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import Table, Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm

# Create your views here.
def book(request):
    tables= Table.objects.all()
    bookings = Booking.objects.all()
    
    
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.name = request.POST.get('name')
            booking.email = request.POST.get('email')
            booking.phone = request.POST.get('phone')
            booking.status = 'Awaiting confirmation'
            booking.guest_count = request.POST.get('guest_count')
            booking.requested_date = request.POST.get('requested_date')
            booking.requested_time  = request.POST.get('requested_time')
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking submitted successfully and awaiting approval'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Booking error, your email or phone is incorrect.'
            )
            
                
            
    booking_form = BookingForm()
    
    return render (
        request,
        "book/book.html",
        {
            'booking_form': booking_form,
            'bookings' : bookings,
         }
                   )