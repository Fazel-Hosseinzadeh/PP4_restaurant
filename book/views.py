from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import Table, Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm

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
            booking.requested_date = request.POST.get('requested_date')
            booking.requested_time  = request.POST.get('requested_time')
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking submitted successfully and awaiting approval'
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
                    print(error)
                    
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