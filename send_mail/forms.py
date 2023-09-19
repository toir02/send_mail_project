from django import forms

from send_mail.models import MailSettings, TextMail, Client, MailingClient


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailSettingsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailSettings
        fields = '__all__'


class TextMailForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = TextMail
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class MailingClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingClient
        fields = '__all__'
