from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class Client(models.Model):
    email = models.CharField(max_length=200, verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('full_name',)
