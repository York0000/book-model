from django.contrib import admin

from category.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(from django.contrib import admin

from category.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
