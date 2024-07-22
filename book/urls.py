from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('edit/<int:id>' , views.edit, name='edit' )
]