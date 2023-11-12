# Generated by Django 3.1.5 on 2023-11-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('thoughts', models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('rating', models.FloatField(max_length=5, verbose_name='Рейтинг')),
                ('count_pages', models.IntegerField(verbose_name='Кол-во страниц')),
                ('created_at', models.DateField(verbose_name='Год издательства')),
                ('posted_at', models.DateTimeField(auto_now=True, verbose_name='Дата публикаций')),
                ('photo', models.ImageField(upload_to='photos/book/%Y/%m/%d/', verbose_name='Фото')),
                ('ISBN', models.IntegerField()),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('author_id', models.ManyToManyField(to='book_app.Authors', verbose_name='Автор')),
            ],
        ),
    ]
