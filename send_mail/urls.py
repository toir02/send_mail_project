from django.urls import path

from send_mail.apps import SendMailConfig

from send_mail.views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', MailListView.as_view(), name='index'),
    path('mail/create/', MailCreateView.as_view(), name='create_mail'),
    path('mail/view/<int:pk>/', MailDetailView.as_view(), name='view_mail'),
    path('mail/edit/<int:pk>/', MailUpdateView.as_view(), name='edit_mail'),
    path('mail/delete/<int:pk>/', MailDeleteView.as_view(), name='delete_mail'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('messages/', TextMailListView.as_view(), name='messages'),
    path('message/create/', TextMailCreateView.as_view(), name='create_message'),
    path('message/view/<int:pk>/', TextMailDetailView.as_view(), name='view_message'),
    path('message/edit/<int:pk>/', TextMailUpdateView.as_view(), name='edit_message'),
    path('message/delete/<int:pk>/', TextMailDeleteView.as_view(), name='delete_message'),
]
