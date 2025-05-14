import os
from django.core.management import BaseCommand

from users import models

class Command(BaseCommand):
    def handle(self, *args, **options):

        admin = models.User.objects.create(
            email='admin@web.top',
            role=models.UserRoles.MODERATOR,
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        admin.set_password(os.getenv("SUPERUSER_PASSWORD"))
        admin.save()
        print('Admin user created.')

        moderator = models.User.objects.create(
            email='moderator@web.top',
            role=models.UserRoles.MODERATOR,
            first_name="Moderator",
            last_name="Moderator",
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

        moderator.set_password(os.getenv("MODERATOR_PASSWORD"))
        moderator.save()
        print('Moderator user created.')

        member = models.User.objects.create(
            email='user@web.top',
            role=models.UserRoles.MEMBER,
            first_name="Member",
            last_name="Member",
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        moderator.set_password(os.getenv("MEMBER_PASSWORD"))
        moderator.save()
        print('Member user created.')