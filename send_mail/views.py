from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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


class MailListView(LoginRequiredMixin, ListView):
    model = MailSettings


class MailCreateView(LoginRequiredMixin, CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:settings')

    def form_valid(self, form):
        return super().form_valid(form)


class MailDetailView(LoginRequiredMixin, DetailView):
    model = MailSettings


class MailUpdateView(LoginRequiredMixin, UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:settings')

    def form_valid(self, form):
        return super().form_valid(form)


class MailDeleteView(LoginRequiredMixin, DeleteView):
    model = MailSettings
    success_url = reverse_lazy('send_mail:settings')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:clients')


class TextMailCreateView(ManagerRequiredMixin, LoginRequiredMixin, CreateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailListView(LoginRequiredMixin, ListView):
    model = TextMail


class TextMailUpdateView(ManagerRequiredMixin, LoginRequiredMixin, UpdateView):
    model = TextMail
    form_class = TextMailForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDeleteView(ManagerRequiredMixin, LoginRequiredMixin, DeleteView):
    model = TextMail

    def get_success_url(self):
        return reverse_lazy('send_mail:messages')


class TextMailDetailView(ManagerRequiredMixin, LoginRequiredMixin, DetailView):
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


def stop_mailing(request, pk):
    if not request.user.groups.filter(name="manager").exists() and not request.user.is_superuser:
        raise PermissionDenied
    mailing = MailingClient.objects.get(pk=pk)
    if mailing.settings.status == 'active' or mailing.settings.status == 'created':
        mailing.settings.status = 'closed'
        mailing.save()
    else:
        mailing.settings.status = 'active'
        mailing.save()
    return redirect(reverse('send_mail:mails'))
