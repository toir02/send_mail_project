import random

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView

from users.forms import *
from users.models import User
from users.services import *


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.save()

        key = random.randint(1000, 9999)
        self.request.session['key'] = key
        user_email = self.request.POST.get('email')
        send_verification_mail(user_email, key)

        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verification')


def verification_user(request):
    key = request.session.get('key')
    user_email = request.user.email
    user = get_object_or_404(User, email=user_email)

    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_key = form.cleaned_data['key']
            if entered_key == key:
                if not user.is_verified:
                    user.is_verified = True
                    user.save()
                return redirect('users:success_verification')
    else:
        form = VerificationForm('Введите верный ключ верификации!')
    return render(request, 'users/verification.html', {'form': form})


def success_verification(request):
    return render(request, 'users/success_verification.html')


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    model = User

    def get_success_url(self):
        return reverse_lazy('send_mail:index')
