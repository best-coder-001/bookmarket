# Generated by Django 3.1.5 on 2023-11-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_auto_20231113_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='genre_id',
            field=models.ManyToManyField(to='book_app.Genres', verbose_name='Жанр'),
        ),
    ]