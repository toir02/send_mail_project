from django.urls import path
from django.views.decorators.cache import cache_page

from send_mail.apps import SendMailConfig

from send_mail.views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', cache_page(30)(index), name='index'),
    path('settings/', MailListView.as_view(), name='settings'),
    path('settings/create/', MailCreateView.as_view(), name='create_settings'),
    path('settings/view/<int:pk>/', MailDetailView.as_view(), name='view_settings'),
    path('settings/edit/<int:pk>/', MailUpdateView.as_view(), name='edit_settings'),
    path('settings/delete/<int:pk>/', MailDeleteView.as_view(), name='delete_settings'),

    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('clients/', ClientListView.as_view(), name='clients'),

    path('messages/', TextMailListView.as_view(), name='messages'),
    path('message/create/', TextMailCreateView.as_view(), name='create_message'),
    path('message/view/<int:pk>/', TextMailDetailView.as_view(), name='view_message'),
    path('message/edit/<int:pk>/', TextMailUpdateView.as_view(), name='edit_message'),
    path('message/delete/<int:pk>/', TextMailDeleteView.as_view(), name='delete_message'),

    path('mails/', MailingClientListView.as_view(), name='mails'),
    path('mails/create', MailingClientCreateView.as_view(), name='create_mail'),
    path('mails/view/<int:pk>', MailingClientDetailView.as_view(), name='view_mail'),
    path('mails/edit/<int:pk>', MailingClientUpdateView.as_view(), name='edit_mail'),
    path('mails/delete/<int:pk>', MailingClientDeleteView.as_view(), name='delete_mail'),

    path('mails/status/<int:pk>/', stop_mailing, name='stop_mailing'),
]
