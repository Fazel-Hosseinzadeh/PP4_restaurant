from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from .models import Table, Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm
from datetime import datetime, timedelta


def book(request):
    """
    Handles the booking process for tables.

    Allows users to submit a booking request through a form. If the form is valid, a new booking is created
    with the provided details. Displays feedback messages based on the success or failure of the form submission.

    **Context**
    ``booking_form``
        An instance of :form:`book.BookingForm` for submitting a new booking.
    ``bookings``
        A queryset of all :model:`book.Booking` instances for display.

    **Template**
    :template:`book/book.html`
    """
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
            booking.table = Table.objects.get(id=request.POST.get('table'))  # Correct assignment of table
            booking.requested_date = request.POST.get('requested_date')
            booking.requested_time  = request.POST.get('requested_time')
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Booking submitted successfully and awaiting approval'
            )
        else:
            # Giving feedback on the reason for failure
            for field, errors in booking_form.errors.items():
                for error in errors:
                    messages.add_message(
                        request, messages.ERROR,
                        f'Error in {field} field: {error}'
                    )

    booking_form = BookingForm()

    return render(
        request,
        "book/book.html",
        {
            'booking_form': booking_form,
            'bookings': bookings,
        }
    )


def edit(request , id):
    """
    Allows users to edit an existing booking.

    Handles the display and updating of a booking instance. If the form is valid after submission, the booking's
    status is set to 'Awaiting confirmation' and the changes are saved. Displays feedback messages based on the
    success or failure of the form submission.

    **Context**
    ``form``
        An instance of :form:`book.BookingForm` pre-filled with the booking's current data for editing.
    ``booking``
        The :model:`book.Booking` instance being edited.

    **Template**
    :template:`book/edit.html`
    """
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
    
    
def delete(request , id):
    """
    Handles the deletion of a booking.

    Deletes the specified booking instance when the request method is POST. After deletion, the user is redirected
    to the booking list view.

    **Context**
    None

    **Template**
    None
    """
    if request.method == 'POST':
        booking = Booking.objects.get(pk=id)
        booking.delete()
    return HttpResponseRedirect(reverse('book'))