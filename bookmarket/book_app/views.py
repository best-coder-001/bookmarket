from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import *
from .utils import *


class IndexPage(ListView):
    pass
