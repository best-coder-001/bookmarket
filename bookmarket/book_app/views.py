from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
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


class UserLoginView(DataMixin, LoginView):
    form_class = AuthenticationForm
    context_object_name = 'form'
    template_name = 'book_app/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация пользователей')
        return dict(list(context.items()) + list(c_def.items()))


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
