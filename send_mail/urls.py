from django.urls import path

from send_mail.apps import SendMailConfig

from send_mail.views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', MailListView.as_view(), name='index'),
    path('mail/create/', MailCreateView.as_view(), name='create_mail'),
    path('mail/view/<int:pk>', MailDetailView.as_view(), name='view_mail'),
    path('mail/edit/<int:pk>', MailUpdateView.as_view(), name='edit_mail'),
    path('mail/delete/<int:pk>', MailDeleteView.as_view(), name='delete_mail'),
]
