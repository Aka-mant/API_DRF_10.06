import os

from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = {
            'admin':{
                'email': 'example@example.com',
                'role': 'admin',
                'lastName': 'Doe',
                'firstName': 'John',
                'password': os.getenv('SUPERUSER_PASSWORD', ''),
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
            'moderator':{
                'email': 'moderator@example.com',
                'role': 'moderator',
                'lastName': 'Moderator',
                'firstName': 'Moderator',
                'password': os.getenv('MODERATOR_PASSWORD', ''),
                'is_staff': True,
                'is_superuser': False,
                'is_active': True,
            },
            'user':{
                'email': 'user@example.com',
                'role': 'user',
                'lastName': 'User',
                'firstName': 'User',
                'password': os.getenv('USER_PASSWORD', ''),
                'is_staff': False,
                'is_superuser': False,
                'is_active': True,
            }

        }

        for user, user_params in users.items():
            cr_user = User.objects.create(
                email = user_params['email'],
                role = user_params['role'],
                lastName = user_params['lastName'],
                firstName = user_params['firstName'],
                password = user_params['password'],
                is_staff = user_params['is_staff'],
                is_superuser = user_params['is_superuser'],
                is_active = user_params['is_active'],

            )
            cr_user.save()
            print(f'User created: {cr_user.email}')


