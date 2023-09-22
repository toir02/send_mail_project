from django.core.mail import send_mail

from config import settings


def send_verification_mail(user_email, key):
    send_mail(subject='Ключ для верификации', message=f'Ваш ключ для верификации аккаунта: {key}',
              from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])
