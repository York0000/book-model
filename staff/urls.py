from django.test import TestCase

# Create your tests here.
from django.urls import path

from staff.views import Staffview

app_name = 'staff'
urlpatterns = [
    path('', Staffview.as_view())
]