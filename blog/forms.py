from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating Comment instances.

    This form uses the Django ModelForm to automatically generate form fields
    based on the Comment model. It includes only the 'body' field.

    Attributes:
        model (Comment): The model associated with this form.
        fields (tuple): The fields to include in the form.
    """

    class Meta:
        model = Comment
        fields = ("body",)
