from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@admin.ru')
        user.set_password('123qwerty123')
        user.save()
