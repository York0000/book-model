from django.test import TestCase

# Create your tests here.
from django.urls import path

from category.views import CategoryaddView, CategoryView, DeletecategoryView, UpdatecategoryView

app_name = 'category'

urlpatterns = [
    path('', CategoryView.as_view(), name='list'),
    path('categoryadd/', CategoryaddView.as_view(), name='create'),
    path('updatecategory/<int:pk>/', UpdatecategoryView.as_view(), name='update'),
    path('deletecategory/<int:pk>/', DeletecategoryView.as_view(), name='delete'),

]
