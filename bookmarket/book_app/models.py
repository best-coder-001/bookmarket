from django.db import models
from django.urls import reverse


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    rating = models.FloatField(max_length=5, verbose_name='Рейтинг')
    count_pages = models.IntegerField(verbose_name='Кол-во страниц')
    created_at = models.DateField(verbose_name='Год издательства')
    posted_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикаций')
    photo = models.ImageField(upload_to='photos/book/%Y/%m/%d/', verbose_name='Фото')
    ISBN = models.IntegerField()
    author_id = models.ManyToManyField('Authors', verbose_name='Автор')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("book_detail", kwargs={'book_slug': self.slug})


class Genres(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    thoughts = models.TextField(max_length=2500)


