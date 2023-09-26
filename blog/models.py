from django.db import models

NULLABLE = {'null': True,
            'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    create_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    count_views = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
