
from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path("", include("home.urls"), name = 'home-urls'),
    path("menus/", include("menus.urls"), name = 'menus-urls'),
    path("post/", include("blog.urls"), name="blog-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
