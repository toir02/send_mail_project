from django import forms

from send_mail.models import MailSettings, TextMail, Client


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
