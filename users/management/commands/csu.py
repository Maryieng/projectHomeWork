from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='kassion.o@yandex.ru',
            first_name='Admin',
            last_name='Sky',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()
