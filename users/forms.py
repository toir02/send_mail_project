from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "available":
                field.widget.attrs['class'] = 'form-control'


class RegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class VerificationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('key',)
