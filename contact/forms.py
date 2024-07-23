from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form class for users to send contact messages.

    Provides a form for users to submit their name, email, and a message. This form is used to capture
    contact messages from users and create `ContactMessage` instances.

    **Fields**
    ``name``
        A text input field for the user's name.
    ``email``
        A text input field for the user's email address.
    ``message``
        A text area field for the user's message.

    **Model**
    :model:`app.ContactMessage`
    """
    class Meta:

        model = ContactMessage
        fields = ('name', 'email', 'message')