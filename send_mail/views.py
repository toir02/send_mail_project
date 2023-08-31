from django.views.generic import ListView

from send_mail.models import Client


class ClientListView(ListView):
    model = Client
