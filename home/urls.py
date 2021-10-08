from django.test import TestCase

# Create your tests here.
from django.urls import path

from home.views import HomeTemplateView, BookDetailView

app_name = 'home'

urlpatterns = [
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('category/<int:pk>/', HomeTemplateView.as_view(), name='category'),
    path('', HomeTemplateView.as_view(), name='home'),
]