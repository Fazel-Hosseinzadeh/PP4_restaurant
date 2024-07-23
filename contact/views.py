from django.shortcuts import render


# Contact views
def contact(request):
    return render (
        request,
        "contact/contact.html",
                   )