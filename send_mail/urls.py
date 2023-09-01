from django.urls import path

from send_mail.apps import SendMailConfig

from send_mail.views import *

app_name = SendMailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='index'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/view/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('client/edit/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
]
