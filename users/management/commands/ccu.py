import os

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Создание пользователей по умолчанию"

    def handle(self, *args, **options):

        users = [
            {
                "email": "example@example.com",
                "password": os.getenv("ADMIN_PASSWORD", "12345678"),
                "role": "admin",
                "firstName": "John",
                "lastName": "Doe",
                "is_superuser": True,
            },
            {
                "email": "moderator@example.com",
                "password": os.getenv("MODERATOR_PASSWORD", "12345678"),
                "role": "moderator",
                "firstName": "Moderator",
                "lastName": "Moderator",
                "is_superuser": False,
                "is_staff": True,
            },
            {
                "email": "user@example.com",
                "password": os.getenv("USER_PASSWORD", "12345678"),
                "role": "member",
                "firstName": "User",
                "lastName": "User",
                "is_superuser": False,
                "is_staff": False,
            },
        ]

        for user_data in users:

            if User.objects.filter(email=user_data["email"]).exists():
                self.stdout.write(
                    self.style.WARNING(
                        f'Пользователь "{user_data["email"]}" уже существует.'
                    )
                )
                continue

            if user_data["is_superuser"]:

                user = User.objects.create_superuser(
                    email=user_data["email"],
                    password=user_data["password"],
                    role=user_data["role"],
                    firstName=user_data["firstName"],
                    lastName=user_data["lastName"],
                )

            else:

                user = User.objects.create_user(
                    email=user_data["email"],
                    password=user_data["password"],
                    role=user_data["role"],
                    firstName=user_data["firstName"],
                    lastName=user_data["lastName"],
                    is_staff=user_data["is_staff"],
                    is_active=True,
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Создан пользователь: {user.email}'
                )
            )