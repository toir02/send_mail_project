from django.contrib import admin

from send_mail.models import Client, Mail, TextMail, LogsMail


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    list_filter = ('full_name',)
    search_fields = ('full_name', 'email')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'status')


@admin.register(TextMail)
class TextMailAdmin(admin.ModelAdmin):
    list_display = ('body', 'topic')
    list_filter = ('topic',)
    search_fields = ('topic',)


@admin.register(LogsMail)
class LogsMailAdmin(admin.ModelAdmin):
    list_display = ('time_last_try', 'status_try', 'answer_mail_server')
