from django.shortcuts import render
from .models import ContactContent
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    Handles the contact form submission and displays contact content.

    Retrieves the most recent `ContactContent` and renders a contact form.
    If the form is submitted
    via POST, it processes the form data to create a new `ContactMessage`
    instance. Provides feedback
    to the user based on the success or failure of the form submission.

    **Context**

    ``contact_form``
        An instance of :form:`contact.ContactForm` for submitting user messages
    ``content``
        The most recent instance of :model:`contact.ContactContent`.

    **Template:**

    :template:`contact/contact.html`
    """
    content = ContactContent.objects.all().order_by("-updated_on").first()
    # request POST
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.name = request.POST.get("name")
            contact.email = request.POST.get("email")
            contact.message = request.POST.get("message")
            contact.read = False
            contact.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thanks for your message. We will contact you soon!",
            )
        else:
            # Giving feedback on the reason for failure
            for field, errors in contact_form.errors.items():
                for error in errors:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        f"Error in {field} field: {error}"
                    )

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form,
            "content": content,
        },
    )
