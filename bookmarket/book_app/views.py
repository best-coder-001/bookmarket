from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import *


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "book_app/auth/login.html")


class IndexPage(ListView):
    pass


class AboutPage(ListView):
    pass


class SendUsPage(ListView):
    pass
