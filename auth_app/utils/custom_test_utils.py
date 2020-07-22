from django_swagger_utils.utils.test import CustomAPITestCase

from auth_app.tests.factories.models import UserFactory


class CustomTestUtils(CustomAPITestCase):
    def create_single_user(self, username: str, password: str):
        user = UserFactory.create(username=username, password=password)
        user.set_password(raw_password=password)
        user.save()
        UserFactory.reset_sequence()
