from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField(max_length=5)
    count_pages = models.IntegerField()
    author_id = models.ManyToManyField('Authors')
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)


    def __str__(self):
        return self.name