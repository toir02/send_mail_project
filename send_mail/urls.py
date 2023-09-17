from django.urls import path

from send_mail.apps import SendMailConfig

from send_mail.views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='index'),
    path('client/create/', MailCreateView.as_view(), name='create_client'),
    path('client/view/<int:pk>', MailDetailView.as_view(), name='view_client'),
    path('client/edit/<int:pk>', MailUpdateView.as_view(), name='edit_client'),
    path('client/delete/<int:pk>', MailDeleteView.as_view(), name='delete_client'),
]
