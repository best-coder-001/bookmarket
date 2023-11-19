from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from book_app import views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('send_us', SendUsView.as_view(), name='send_us'),
    path('detail/<slug:book_slug>', BookDetailView.as_view(), name='book_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup', UserRegistrationView.as_view(), name='signup'),
    path('add_book', BookAddView.as_view(), name='add_book'),
    # path('forgot_password', UserForgotPasswordView.as_view(), name='forgot_psw')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
