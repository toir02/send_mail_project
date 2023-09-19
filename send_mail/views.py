from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from send_mail.forms import MailSettingsForm, ClientForm, TextMailForm
from send_mail.models import MailSettings, TextMail, Client


class MailListView(ListView):
    model = MailSettings
    template_name = 'send_mail/mail_list.html'


class MailCreateView(CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_form.html'

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     send_mailing(self.object)
    #     return response


class MailDetailView(DetailView):
    model = MailSettings
    template_name = 'send_mail/mail_detail.html'


class MailUpdateView(UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_form.html'

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     send_mailing(self.object)
    #     return response


class MailDeleteView(DeleteView):
    model = MailSettings
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_confirm_delete.html'
