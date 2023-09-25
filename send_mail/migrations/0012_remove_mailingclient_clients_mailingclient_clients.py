# Generated by Django 4.2.4 on 2023-09-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0011_remove_mailingclient_clients_mailingclient_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingclient',
            name='clients',
        ),
        migrations.AddField(
            model_name='mailingclient',
            name='clients',
            field=models.ManyToManyField(to='send_mail.client', verbose_name='клиент'),
        ),
    ]
