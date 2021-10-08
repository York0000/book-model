from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from books.models import BookModel


class FormsModel(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BookModel
        exclude = ['created_at', 'update_at']
