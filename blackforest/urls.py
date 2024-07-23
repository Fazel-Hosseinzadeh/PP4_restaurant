
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
