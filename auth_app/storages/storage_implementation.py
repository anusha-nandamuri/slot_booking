from auth_app.interactors.storages.dtos import UserIdentityDto
from auth_app.interactors.storages.storage_interface import StorageInterface
from auth_app.models import User


class StorageImplementation(StorageInterface):
    def validate_user_name(self, username: str):
        from django.core.exceptions import ObjectDoesNotExist
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            from auth_app.exceptions.common_exceptions import InvalidUsername
            raise InvalidUsername

    def valid_password_return_user_id_and_role_dto(
            self, username: str, password: str
    ) -> UserIdentityDto:
        user = User.objects.get(username=username)
        is_password_match = user.check_password(password)
        if is_password_match:
            user_identity_dto = UserIdentityDto(
                user_id=user.id,
                is_admin=user.is_admin
            )
        else:
            from auth_app.interactors.login_interactor import InvalidPassword
            raise InvalidPassword
        return user_identity_dto

    def signup_user(self, username: str, password: str):
        User.objects.create_user(username=username, password=password)


