from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import Table, Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm
from datetime import datetime, timedelta

# Booking function
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
            booking.table_reserved = request.POST.get('table')
            booking.requested_date = request.POST.get('requested_date')
            booking.requested_time  = request.POST.get('requested_time')
            
            other_bookings_book = False #for checking if others booked already
            if bookings:
                for other_booking in bookings:
                    if other_booking.table == booking.table and (
                        (other_booking.requested_date == booking.requested_date and
                        other_booking.requested_time >= booking.requested_time and
                        other_booking.requested_time < (booking.requested_time + timedelta(hours=2)))):
                        other_bookings_book = True
                        
            if not other_bookings_book:
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Booking submitted successfully and awaiting approval'
                )
                #update bookings list with new booking 
                bookings = Booking.objects.all()
                
            else:
                messages.add_message(
                    request, messages.SUCCESS,
                    'This table is alredy booked '
                )
                
                        
                       
        else:
            
            # Giving feedback of the reason of failure
            if not booking_form.is_valid():
                for error in booking_form.errors:
                    if error == '__all__':
                        continue
                    messages.add_message(
                        request, messages.ERROR,
                        f'Error in {error} field. Booking unsuccessful'
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
    
# Edit booking function
def edit(request , id):
    if request.method == "POST":

        booking = Booking.objects.get(pk=id)
        form = BookingForm(request.POST , instance = booking)
        if form.is_valid():
            booking.status ='Awaiting confirmation'
            form.save() 
            messages.add_message(
                request, messages.SUCCESS,
                'Booking updated successfully and awaiting approval'
                )
            return HttpResponseRedirect (reverse('book'),
                        {
                            'form': form,
                            'booking': booking,
                        }
                        )
                        
           
    else:
        booking = Booking.objects.get(pk=id)
        form = BookingForm(instance = booking)
        return render (request, 'book/edit.html',
                        {
                            'form': form,
                            'booking': booking
                        }
                        )
        
#Delete booking function
def delete(request , id):
    if request.method == 'POST':
        booking = Booking.objects.get(pk=id)
        booking.delete()
    return HttpResponseRedirect(reverse('book'))