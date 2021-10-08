from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, ListView, CreateView

from category.forms import CategoryModelforms
from category.models import CategoryModel


class CategoryView(LoginRequiredMixin, ListView):
    template_name = 'category.html'
    model = CategoryModel

    def get_context_data(self, **kwargs):
        context = super().get_context_datfrom django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, ListView, CreateView

from category.forms import CategoryModelforms
from category.models import CategoryModel


class CategoryView(LoginRequiredMixin, ListView):
    template_name = 'category.html'
    model = CategoryModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category'
        return context


class CategoryaddView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CategoryModelforms

    def get_success_url(self):
        return reverse('category:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categoryadd'
        return context


class UpdatecategoryView(LoginRequiredMixin, UpdateView):
    model = CategoryModel
    form_class = CategoryModelforms
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('category:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Category'
        return context


class DeletecategoryView(LoginRequiredMixin, DeleteView):
    model = CategoryModel

    def get_success_url(self):
        return reverse('category:list')
