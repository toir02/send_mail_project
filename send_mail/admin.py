from django.contrib import admin

from send_mail.models import Client, MailSettings, TextMail, LogMail


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    list_filter = ('full_name',)
    search_fields = ('full_name', 'email')


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'period', 'status')


@admin.register(TextMail)
class TextMailAdmin(admin.ModelAdmin):
    list_display = ('body', 'topic')
    list_filter = ('topic',)
    search_fields = ('topic',)


@admin.register(LogMail)
class LogMailAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'response')
