from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)
    birthyear = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    pages = models.IntegerField()
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
