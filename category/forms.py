from django import forms

from category.models import CategoryModel


class CategoryModelfofrom django import forms

from category.models import CategoryModel


class CategoryModelforms(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title']