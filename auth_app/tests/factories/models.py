import factory

from auth_app.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence(lambda a: f'user{a + 1}')
    password = factory.sequence(lambda a: f'password{a + 1}')
