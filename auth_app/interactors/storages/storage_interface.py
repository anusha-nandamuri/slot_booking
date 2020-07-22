import abc

from auth_app.interactors.storages.dtos import UserIdentityDto


class StorageInterface:
    @abc.abstractmethod
    def validate_user_name(self, username: str):
        pass

    @abc.abstractmethod
    def valid_password_return_user_id_and_role_dto(self, username: str, password: str) -> UserIdentityDto:
        pass

    @abc.abstractmethod
    def signup_user(self, username: str, password: str):
        pass

