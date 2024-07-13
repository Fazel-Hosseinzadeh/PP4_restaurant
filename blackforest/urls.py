
from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path("", include("home.urls"), name = 'home-urls'),
    path('admin/', admin.site.urls),
]
