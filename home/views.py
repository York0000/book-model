from math import ceil

from django.views.generic import ListView, DetailView

from books.models import BookModel


class HomeTemplateView(ListView):
    template_name = 'home.html'
    model = BookModel
    paginate_by = 3

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            returfrom math import ceil

from django.views.generic import ListView, DetailView

from books.models import BookModel


class HomeTemplateView(ListView):
    template_name = 'home.html'
    model = BookModel
    paginate_by = 3

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return BookModel.objects.filter(category_id=pk).order_by('-pk')
        else:
            return BookModel.objects.order_by('-pk')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     x = ceil(BookModel.objects.count() / self.paginate_by)
    #
    #     context['range'] = range(x)
    #     return context


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = BookModel
