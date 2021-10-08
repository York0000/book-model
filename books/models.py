from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from image_cropping import ImageRatioField

from author.models import AuthorModel

from category.models import CategoryModel


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    page_count = models.IntegerField(blank=True,
                                     validators=[MinValueValidator(50), MaxValueValidator(100)])

    cover = models.ImageField(upload_to='covers', null=True)
    cropping = ImageRatioField('cover', '430x360', free_crop=True)

    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT,
                               related_name='books', null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,
                                 related_name='books')

    description = RichTextUploadingField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
