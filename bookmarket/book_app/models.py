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
    genre_id = models.ManyToManyField('Genres', verbose_name='Жанр')
    catalog_id = models.ForeignKey('Catalog', verbose_name='Каталог',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("book_detail", kwargs={'book_slug': self.slug})


class Catalog(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Genres(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Authors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class FeedBack(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    thoughts = models.TextField(max_length=2500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'Обратная связь'
