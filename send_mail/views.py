from random import sample

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from send_mail.forms import MailSettingsForm, ClientForm, TextMailForm, MailingClientForm
from send_mail.models import MailSettings, TextMail, Client, MailingClient


class ManagerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name="manager").exists():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def index(request):
    blog = Blog.objects.all()
    mailing_is_active = MailSettings.objects.filter(status='active')
    client_mailing = MailingClient.objects.all()
    unique_clients = client_mailing.values_list('clients', flat=True).distinct()
    random_articles = sample(list(blog), k=min(len(blog), 3))

    context = {
        'random_articles': random_articles,
        'total_mailings': len(client_mailing),
        'active_mailings': len(mailing_is_active),
        'unique_clients': len(unique_clients)
    }

    return render(request, 'send_mail/home.html', context)


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


class TextMailCreateView(ManagerRequiredMixin, CreateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailListView(ListView):
    model = TextMail


class TextMailUpdateView(ManagerRequiredMixin, UpdateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDeleteView(ManagerRequiredMixin, DeleteView):
    model = TextMail

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDetailView(ManagerRequiredMixin, DetailView):
    model = TextMail


class MailingClientListView(ListView):
    model = MailingClient

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return MailingClient.objects.none()

        if self.request.user.groups.filter(name="manager").exists() or self.request.user.is_superuser:
            return MailingClient.objects.all()

        return MailingClient.objects.filter(created_by=self.request.user)


class MailingClientCreateView(ManagerRequiredMixin, CreateView):
    model = MailingClient
    form_class = MailingClientForm

    def form_valid(self, form):
        mailing_client = form.save(commit=False)
        selected_client_ids = self.request.POST.getlist('selected_clients')

        if selected_client_ids:
            mailing_client.created_by = self.request.user
            mailing_client.save()
            mailing_client.clients.set(selected_client_ids)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')


class MailingClientDetailView(ManagerRequiredMixin, DetailView):
    model = MailingClient


class MailingClientUpdateView(ManagerRequiredMixin, UpdateView):
    model = MailingClient
    form_class = MailingClientForm

    def form_valid(self, form):
        mailing_client = form.save(commit=False)
        selected_client_ids = self.request.POST.getlist('selected_clients')

        if selected_client_ids:
            mailing_client.created_by = self.request.user
            mailing_client.save()
            mailing_client.clients.set(selected_client_ids)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        mailing_client = self.get_object()
        context['selected_clients'] = mailing_client.clients.all()
        return context

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')


class MailingClientDeleteView(ManagerRequiredMixin, DeleteView):
    model = MailingClient

    def get_success_url(self):
        return reverse_lazy('send_mail:mails')
