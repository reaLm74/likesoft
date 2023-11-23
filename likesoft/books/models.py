from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

LEN_ISBN = 13


class Books(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название'
    )
    author = models.CharField(
        max_length=60,
        verbose_name='Автор'
    )
    pub_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Год издания'
    )
    isbn = models.CharField(
        max_length=LEN_ISBN,
        unique=True,
        verbose_name='ISBN',
    )

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
