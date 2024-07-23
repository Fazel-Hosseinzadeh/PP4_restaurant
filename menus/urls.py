from django.urls import path
from menus import views


urlpatterns = [
    path("", views.menus, name="menus"),
]
