# Generated by Django 4.2.4 on 2023-09-18 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0004_remove_textmail_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmail',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='send_mail.mailsettings', verbose_name='настройки'),
        ),
    ]
