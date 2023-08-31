from django.urls import path

from send_mail.apps import SendMailConfig
from send_mail.views import index

app_name = SendMailConfig.name

urlpatterns = [
    path('', index, name='index')
]
