from auth_app.interactors.dtos import AuthenticationDto
from auth_app.interactors.presenters.presenter_interface import LoginPresenterInterface
from auth_app.interactors.storages.storage_interface import StorageInterface
from common.oauth2_storage import OAuth2SQLStorage


class InvalidPassword(Exception):
    pass


class LoginInteractor:
    def __init__(self, storage: StorageInterface, oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def login_wrapper(self, username: str, password: str, presenter: LoginPresenterInterface):
        from auth_app.exceptions.common_exceptions import InvalidUsername
        try:
            authentication_dto = self.login_interactor(username=username, password=password)
        except InvalidUsername:
            return presenter.get_username_not_found_http_response()
        except InvalidPassword:
            return presenter.get_password_bad_request_http_response()
        http_response = presenter.get_login_response(authentication_dto)

        return http_response

    def login_interactor(self, username: str, password: str):
        self.storage.validate_user_name(username=username)
        user_identity_dto = self.storage.valid_password_return_user_id_and_role_dto(
            username=username, password=password
        )
        from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
        oauth_service_obj = OAuthUserAuthTokensService(oauth2_storage=self.oauth_storage)
        access_token_dto = oauth_service_obj.create_user_auth_tokens(
            user_id=user_identity_dto.user_id
        )
        authentication_dto = AuthenticationDto(
            access_token=access_token_dto.access_token,
            is_admin=user_identity_dto.is_admin
        )
        return authentication_dto
