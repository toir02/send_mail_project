from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail

from send_mail.models import *


def send_mailing(mail_settings, client_mailing):
    try:
        send_mail(
            mail_settings.message.topic,
            mail_settings.message.body,
            settings.EMAIL_HOST_USER,
            [client_mailing.client.email],
            fail_silently=False,
        )
        status = True
        response = None
    except Exception as ex:
        status = False
        response = str(ex)

    LogMail.objects.create(
        status=status,
        settings=mail_settings,
        client_id=client_mailing.client_id,
        response=response
    )


def send_mails():
    current_time = datetime.utcnow()
    current_date = datetime.utcnow().date()
    for mailing_settings in MailSettings.objects.filter(status='active'):

        start_date = datetime.combine(current_date, mailing_settings.start_time)
        current_stop_date = datetime.combine(current_date, mailing_settings.end_time)
        stop_date = current_stop_date if mailing_settings.end_time > mailing_settings.start_time else (current_stop_date
                                                                                                       + timedelta
                                                                                                       (hours=24))
        if start_date < current_time < stop_date:

            client_mailing = mailing_settings.clientmailing_set.all()
            for client in client_mailing:
                logs = LogMail.objects.filter(
                    settings=mailing_settings, client=client.client
                )

                if logs.exists():
                    last_try_date = logs.order_by('-date_time').first().date_time.replace(tzinfo=None)

                    if mailing_settings.period == 'D':
                        if (current_time - last_try_date).days >= 1:
                            send_mailing(mailing_settings, client)

                    elif mailing_settings.mailing_period == 'W':
                        if (current_time - last_try_date).days >= 7:
                            send_mailing(mailing_settings, client)

                    elif mailing_settings.mailing_period == 'M':

                        if (current_time - last_try_date).days >= 30:
                            send_mailing(mailing_settings, client)

                else:
                    send_mailing(mailing_settings, client)
