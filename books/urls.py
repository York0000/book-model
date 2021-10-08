from django.test import TestCase

# Create your tests here.
from django.urls import path

from books.views import Booklistview, CreateBookView, UpdatebookView, DeletebookView

app_name = 'books'

urlpatterns = [
    path('', Booklistview.as_view(), name='list'),
    path('create/', CreateBookView.as_view(), name='create'),
    path('updatebook/<int:pk>/', UpdatebookView.as_view(), name='update'),
    path('delete/<int:pk>/', DeletebookView.as_view(), name='delete'),
]
