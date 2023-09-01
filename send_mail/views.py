from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from send_mail.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('send_mail:index')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('send_mail:index')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('send_mail:index')
