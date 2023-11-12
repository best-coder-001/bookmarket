from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import *
from .forms import *


class IndexView(DataMixin, ListView):
    model = Books
    template_name = 'book_app/index.html'
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, ListView):
    model = Books
    template_name = 'book_app/about.html'
    context_object_name = "books"


class SendUsView(DataMixin, CreateView):
    form_class = FeedBackForm
    template_name = 'book_app/send_us.html'
    success_url = reverse_lazy("TODO: Implement me...")
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поделись впечатлениями о сайте!')
        return dict(list(context.items()) + list(c_def.items()))


class BookDetailView(DataMixin, DetailView):
    model = Books
    template_name = 'book_app/book_detail.html'
    context_object_name = "book"
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f'Книга - {self.model.objects.get(slug=self.slug_url_kwarg).name}')
        return dict(list(context.items()) + list(c_def.items()))
