from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from books.forms import FormsModel
from books.models import BookModel


class Booklistview(LoginRequiredMixin, ListView):
    template_name = 'books_list.html'

    from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from books.forms import FormsModel
from books.models import BookModel


class Booklistview(LoginRequiredMixin, ListView):
    template_name = 'books_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return BookModel.objects.filter(Q(title__icontains=q) |
                                        Q(author__name__icontains=q) |
                                        Q(category__title__icontains=q)
                                        )


class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = FormsModel

    def get_success_url(self):
        return reverse('books:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'create book'
        return context


class UpdatebookView(LoginRequiredMixin, UpdateView):
    model = BookModel
    form_class = FormsModel
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('books:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update book'
        return context


class DeletebookView(LoginRequiredMixin, DeleteView):
    model = BookModel

    def get_success_url(self):
        return reverse('books:list')





