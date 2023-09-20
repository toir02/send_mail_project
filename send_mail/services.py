from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail

from send_mail.models import *


def send_mailing(mailing):
    if 'active' not in mailing.status:
        return

    current_time = datetime.now()
    current_date = datetime.now().date()
    start_date = datetime.combine(current_date, mailing.start_time)
    current_stop_date = datetime.combine(current_date, mailing.end_time)
    stop_date = current_stop_date if mailing.end_time > mailing.start_time else (
                current_stop_date + timedelta(hours=24))
    if start_date > current_time or current_time > stop_date:
        return

    client_list = MailingClient.objects.filter(mailing_id=mailing.id)

    for client in client_list:
        try:
            send_mail(
                mailing.message.topic,
                mailing.message.body,
                settings.EMAIL_HOST_USER,
                [client.client.email],
                fail_silently=False,
            )
            status = 'success'
            response = None
        except Exception as ex:
            status = 'fail'
            response = str(ex)

        log = LogMail(settingns=mailing, status=status, response=response)
        log.save()


def run_mail(period):
    mailing = MailSettings.objects.filter(status='active', period=period)
    for mail in mailing:
        send_mailing(mail)
