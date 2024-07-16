from django.shortcuts import render
from .models import Table
from .forms import BookingForm

# Create your views here.
def book(request):
    tables= Table.objects.all()
    booking_form = BookingForm()
    
    return render (
        request,
        "book/book.html",
        {'booking_form': booking_form}
                   )