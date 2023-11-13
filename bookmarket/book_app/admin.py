from django.contrib import admin
from .models import *


class AdminBookModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class AdminGenresModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class AdminAuthorsModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class AdminFeedBacksModel(admin.ModelAdmin):
    pass


class AdminCatalogModel(admin.ModelAdmin):
    pass


admin.site.register(Books, AdminBookModel)
admin.site.register(Genres, AdminGenresModel)
admin.site.register(Authors, AdminAuthorsModel)
admin.site.register(FeedBack, AdminFeedBacksModel)
admin.site.register(Catalog, AdminCatalogModel)
