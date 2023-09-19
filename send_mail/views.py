from django.forms import inlineformset_factory
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        text_mail_formset = inlineformset_factory(MailSettings, TextMail, fields=['topic', 'body'], extra=1,
                                                  can_delete=False)
        client_form_set = inlineformset_factory(MailSettings, Client, fields=['email', 'full_name', 'comment'], extra=1,
                                                can_delete=False)

        context['text_mail_formset'] = text_mail_formset(instance=self.object)
        context['client_formset'] = client_form_set(instance=self.object)

        return context

    def form_valid(self, form):
        client_form = ClientForm(self.request.POST)
        text_mail_form = TextMailForm(self.request.POST)
        mail_settings_form = MailSettingsForm(self.request.POST)

        if client_form.is_valid() and text_mail_form.is_valid() and mail_settings_form.is_valid():
            client = client_form.save()
            text_mail = text_mail_form.save(commit=False)
            text_mail.settings = mail_settings_form.save()
            text_mail.save()
            client.mailsettings_set.add(text_mail.settings)

        return super().form_valid(form)


class MailDetailView(DetailView):
    model = MailSettings
    template_name = 'send_mail/mail_detail.html'


class MailUpdateView(UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        text_mail_formset = inlineformset_factory(MailSettings, TextMail, fields=['topic', 'body'], extra=1,
                                                  can_delete=False)
        client_form_set = inlineformset_factory(MailSettings, Client, fields=['email', 'full_name', 'comment'], extra=1,
                                                can_delete=False)

        context['text_mail_formset'] = text_mail_formset(instance=self.object)
        context['client_formset'] = client_form_set(instance=self.object)

        return context

    def form_valid(self, form):
        client_form = ClientForm(self.request.POST)
        text_mail_form = TextMailForm(self.request.POST)
        mail_settings_form = MailSettingsForm(self.request.POST)

        if client_form.is_valid() and text_mail_form.is_valid() and mail_settings_form.is_valid():
            client = client_form.save()
            text_mail = text_mail_form.save()
            text_mail.settings = mail_settings_form.save()
            text_mail.save()
            client.mailsettings_set.add(text_mail.settings)

        return super().form_valid(form)


class MailDeleteView(DeleteView):
    model = MailSettings
    success_url = reverse_lazy('send_mail:index')
    template_name = 'send_mail/mail_confirm_delete.html'
