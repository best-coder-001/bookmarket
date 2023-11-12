from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('about',AboutView.as_view(),name='about'),
    path('send_us', SendUsView.as_view(),name='send_us'),
    path('detail/<slug:book_slug>',BookDetailView.as_view(),name='book_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
