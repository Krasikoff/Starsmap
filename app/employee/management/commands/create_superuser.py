from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from employee.models import User
from starsmap import settings

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = 'admin'
                print('Creating account for %s (%s)' % (username, email))
                User.objects.create_superuser(
                    email=email, username=username, password=password
                )
        else:
            print('В базе уже есть пользователи.')
