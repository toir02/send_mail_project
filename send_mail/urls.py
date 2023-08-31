from django.urls import path

from send_mail.apps import SendMailConfig

from views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='index')
]
