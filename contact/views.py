from django.shortcuts import render
from .models import ContactContent

# Contact views
def contact(request):
    content = ContactContent.objects.all().order_by('-updated_on').first()
    
    
    return render (
        request,
        "contact/contact.html",
        {
        "content": content,
        }
                   )