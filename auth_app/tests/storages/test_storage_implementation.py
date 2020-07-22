import pytest

from auth_app.interactors.login_interactor import InvalidPassword
from auth_app.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_user_name_invalid_user_name_raises_exception():
    # Arrange
    username = "user1"
    storage = StorageImplementation()

    # Act
    from auth_app.exceptions.common_exceptions import InvalidUsername
    with pytest.raises(InvalidUsername):
        storage.validate_user_name(username=username)


@pytest.mark.django_db
def test_validate_user_name_valid_user_name_return_none(create_user):
    # Arrange
    from auth_app.models import User
    user = User.objects.all()
    print(user)
    username = "user1"
    storage = StorageImplementation()
    expected_return_value = None

    # Act
    return_value = storage.validate_user_name(username=username)

    # Assert
    assert expected_return_value == return_value


class TestValidPasswordReturnUserIdAndRoleDto:
    @pytest.mark.django_db
    def test_invalid_password_raises_exception(self, create_user):
        # Arrange
        from auth_app.models import User
        user = User.objects.all()
        print(user)
        username = "user2"
        password = "password1"
        storage = StorageImplementation()

        # Act
        with pytest.raises(InvalidPassword):
            storage.valid_password_return_user_id_and_role_dto(
                username=username, password=password
            )

    @pytest.mark.django_db
    def test_valid_password_return_user_id_and_role_dto(self, create_user, snapshot):
        # Arrange
        from auth_app.models import User
        user = User.objects.all()
        user1 = User.objects.get(username="user2")
        print(user)
        username = "user2"
        password = "password2"
        storage = StorageImplementation()

        # Act
        user_identity_dto = storage.valid_password_return_user_id_and_role_dto(
            username=username, password=password
        )

        # Assert
        snapshot.assert_match(user_identity_dto, 'dto')


class TestCreateUser:
    @pytest.mark.django_db
    def test_user_created(self):
        # Arrange
        username = "user1"
        password = "password1"
        storage = StorageImplementation()

        # Act
        storage.signup_user(username=username, password=password)

        # Assert
        from auth_app.models import User
        user = User.objects.get(username=username)
        assert user.check_password(raw_password=password) == True
