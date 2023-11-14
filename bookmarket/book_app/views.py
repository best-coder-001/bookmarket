from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .utils import *
from .forms import *


class IndexView(DataMixin, ListView):
    model = Books
    template_name = 'index.html'
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Books.objects.all().prefetch_related('author_id')


class IndexPage(ListView):
    pass


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
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class UserRegistrationView(DataMixin, CreateView):
    form_class = UserRegisterForm
    context_object_name = 'form'
    template_name = 'book_app/registration.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация пользователей')
        return dict(list(context.items()) + list(c_def.items()))


def login_user_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['remember_me']:
                request.session.set_expiry(604800)
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request,'book_app/auth/login.html',context=context)


class BookAddView(DataMixin, CreateView):
    form_class = AddBookForm
    context_object_name = 'form'
    template_name = 'book_app/add_book.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление книг')
        return dict(list(context.items()) + list(c_def.items()))


class UserForgotPasswordView(DataMixin, FormView):
    form_class = UserForgotPasswordForm
    template_name = 'book_app/forgot_psw.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Забыл пароль')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('home')
