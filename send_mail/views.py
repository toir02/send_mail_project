from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from send_mail.models import MailSettings


class MailListView(ListView):
    model = MailSettings
    template_name = 'send_mail/mail_list.html'


class MailCreateView(CreateView):
    model = MailSettings
    fields = ('message', 'time', 'status', 'period')
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_form.html'


class MailDetailView(DetailView):
    model = MailSettings
    template_name = 'send_mail/mail_detail.html'


class MailUpdateView(UpdateView):
    model = MailSettings
    fields = ('message', 'time', 'status', 'period')
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_form.html'


class MailDeleteView(DeleteView):
    model = MailSettings
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_confirm_delete.html'
