from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        retufrom django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
