# Generated by Django 4.2.4 on 2023-09-03 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0004_alter_mail_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LogsMail',
            new_name='LogMail',
        ),
        migrations.RenameModel(
            old_name='Mail',
            new_name='MailSettings',
        ),
    ]
