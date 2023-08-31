from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('full_name',)


class Mail(models.Model):

    CHOICES = (
        ('D', 'Каждый день'),
        ('W', 'Каждую неделю'),
        ('M', 'Каждый месяц')
    )

    time = models.TimeField(verbose_name='время рассылки', default='09:00')
    interval = models.CharField(verbose_name='периодичность', choices=CHOICES)
    status = models.CharField(max_length=10, verbose_name='статус рассылки')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class TextMail(models.Model):
    topic = models.CharField(max_length=200, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='письмо')

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class LogsMail(models.Model):
    time_last_try = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_try = models.CharField(max_length=10, verbose_name='статус последней попытки')
    answer_mail_server = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)

    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='письмо')

    class Meta:
        verbose_name = 'Логи сообщения'
        verbose_name_plural = 'Логи сообщения'
