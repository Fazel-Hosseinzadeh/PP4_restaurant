from django.db import models


class ContactContent(models.Model):
    """
    Stores content for the contact page.

    Contains the title and content for the contact section of the website. The `updated_on` field
    automatically tracks when the content was last modified.

    **Fields**
    ``title``
        A CharField to store the title of the content, with a maximum length of 200 characters.
    ``updated_on``
        A DateTimeField that automatically updates to the current date and time whenever the content is modified.
    ``content``
        A TextField to store the main body of the content.

    **Methods**
    ``__str__``
        Returns the title of the content.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """
    Stores messages sent by users through the contact form.

    Captures user-submitted messages including the sender's name, email, and the message content.
    The `read` field indicates whether the message has been read by an administrator.

    **Fields**
    ``name``
        A CharField to store the sender's name, with a maximum length of 50 characters.
    ``email``
        An EmailField to store the sender's email address.
    ``message``
        A TextField to store the content of the message.
    ``read``
        A BooleanField to indicate whether the message has been read by an administrator.

    **Methods**
    ``__str__``
        Returns a string representation of the message, prefixed with the sender's name.
    """

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
