import django
from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    mail = models.ForeignKey('MailingClient', on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

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

    start_time = models.TimeField(verbose_name='время старта рассылки', default='09:00')
    end_time = models.TimeField(verbose_name='время окончания рассылки', default='00:00')
    period = models.CharField(max_length=30, verbose_name='периодичность', choices=PERIOD_CHOICES)
    status = models.CharField(max_length=10, verbose_name='статус рассылки', choices=STATUS_CHOICES, default='created')

    message = models.ForeignKey('TextMail', on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class TextMail(models.Model):
    topic = models.CharField(max_length=200, verbose_name='тема')
    body = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class LogMail(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status = models.BooleanField(default=True, verbose_name='статус последней попытки')
    response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)

    settings = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='настройка')

    class Meta:
        verbose_name = 'Логи сообщения'
        verbose_name_plural = 'Логи сообщения'


class MailingClient(models.Model):
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    settings = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='настройка', **NULLABLE)

    created_by = models.ForeignKey(django.conf.settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   verbose_name='создано пользователем', **NULLABLE)

    def __str__(self):
        return f'{self.clients} {self.settings}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
