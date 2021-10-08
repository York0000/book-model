from django.contrib import admin
from image_cropping import ImageCroppingMixin

from books.models import BookModel


@admin.register(Bofrom django.contrib import admin
from image_cropping import ImageCroppingMixin

from books.models import BookModel


@admin.register(BookModel)
class BookModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'page_count', 'created_at']
    list_filter = ['created_at']


