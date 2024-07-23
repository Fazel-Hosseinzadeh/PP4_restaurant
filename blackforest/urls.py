"""
URL configuration for the Black Forest Restaurant Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path("", include("home.urls"), name = 'home-urls'),
    path("menus/", include("menus.urls"), name = 'menus-urls'),
    path("blog/", include("blog.urls"), name="blog-urls"),
    path("book/", include("book.urls"), name="book-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
