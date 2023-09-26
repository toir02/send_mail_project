import json

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from send_mail.forms import MailSettingsForm, ClientForm, TextMailForm, MailingClientForm, ClientSelectionForm
from send_mail.models import MailSettings, TextMail, Client, MailingClient


class MailListView(ListView):
    model = MailSettings


class MailCreateView(CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:settings')

    def form_valid(self, form):
        return super().form_valid(form)


class MailDetailView(DetailView):
    model = MailSettings


class MailUpdateView(UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:settings')

    def form_valid(self, form):
        return super().form_valid(form)


class MailDeleteView(DeleteView):
    model = MailSettings
    success_url = reverse_lazy('send_mail:settings')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class ClientListView(ListView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class TextMailCreateView(CreateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailListView(ListView):
    model = TextMail


class TextMailUpdateView(UpdateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDeleteView(DeleteView):
    model = TextMail

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDetailView(DetailView):
    model = TextMail


class MailingClientListView(ListView):
    model = MailingClient


class MailingClientCreateView(CreateView):
    model = MailingClient
    form_class = MailingClientForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = Client.objects.all()
        context['clients'] = clients

        return context

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')


class MailingClientDetailView(DetailView):
    model = MailingClient


class MailingClientUpdateView(UpdateView):
    model = MailingClient
    form_class = MailingClientForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        clients = Client.objects.all()
        context['clients'] = clients

        return context

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')


class MailingClientDeleteView(DeleteView):
    model = MailingClient

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')
