from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from book_app import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
