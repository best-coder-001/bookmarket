from django.contrib import admin
from .models import *


class AdminBookModel(admin.ModelAdmin):
    pass


class AdminGenresModel(admin.ModelAdmin):
    pass


class AdminAuthorsModel(admin.ModelAdmin):
    pass


admin.site.register(Books, AdminBookModel)
admin.site.register(Genres, AdminGenresModel)
admin.site.register(Authors, AdminAuthorsModel)
