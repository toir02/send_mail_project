from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('full_name',)


class MailSettings(models.Model):

    PERIOD_CHOICES = (
        ('D', 'Каждый день'),
        ('W', 'Каждую неделю'),
        ('M', 'Каждый месяц')
    )

    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('active', 'Запущена'),
        ('closed', 'Завершена')
    )

    time = models.TimeField(verbose_name='время рассылки', default='09:00')
    period = models.CharField(max_length=30, verbose_name='периодичность', choices=PERIOD_CHOICES)
    status = models.CharField(max_length=10, verbose_name='статус рассылки', choices=STATUS_CHOICES, default='created')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class TextMail(models.Model):
    topic = models.CharField(max_length=200, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    mail = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='письмо')

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class LogMail(models.Model):
    time_last_try = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_try = models.CharField(max_length=10, verbose_name='статус последней попытки')
    answer_mail_server = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)

    mail = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='письмо')

    class Meta:
        verbose_name = 'Логи сообщения'
        verbose_name_plural = 'Логи сообщения'


class MailingClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    settings = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='настройка')

    def __str__(self):
        return f'{self.client} {self.settings}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
