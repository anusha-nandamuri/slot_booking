from auth_app.interactors.presenters.presenter_interface import SignupPresenterInterface
from auth_app.interactors.storages.storage_interface import StorageInterface


class UsernameAlreadyExists(Exception):
    pass


class SignupInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def signup_wrapper(self, username: str, password: str, presenter: SignupPresenterInterface):
        try:
            self.signup_interactor(username=username, password=password)
        except UsernameAlreadyExists:
            http_responce = presenter.get_user_name_already_exist_bad_request_response()
            return http_responce
        http_response = presenter.get_signup_success_responce()
        return http_response

    def signup_interactor(self, username: str, password: str):
        is_username_already_exists = True
        from auth_app.exceptions.common_exceptions import InvalidUsername
        try:
            self.storage.validate_user_name(username=username)
        except InvalidUsername:
            is_username_already_exists = False

        if is_username_already_exists:
            raise UsernameAlreadyExists
        self.storage.signup_user(username=username, password=password)
