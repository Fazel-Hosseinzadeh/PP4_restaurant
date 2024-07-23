from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """
    Renders the home page of the website.

    Displays the home page with content specific to the homepage layout.

    **Context**

    None

    **Template:**

    :template:`home/home.html`
    """
    return render (
        request,
        "home/home.html",
                   )