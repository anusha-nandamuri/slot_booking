import pytest

from auth_app.tests.factories.models import UserFactory


@pytest.fixture
def create_user():
    user = UserFactory.create()
    user.set_password(user.password)
    user.save()
    UserFactory.reset_sequence(1)


