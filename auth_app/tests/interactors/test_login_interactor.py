import unittest
from unittest import mock
from unittest.mock import patch

from auth_app.interactors.presenters.presenter_interface \
    import LoginPresenterInterface
from auth_app.interactors.storages.storage_interface \
    import StorageInterface
from auth_app.interactors.login_interactor import LoginInteractor
from common.oauth2_storage import OAuth2SQLStorage

from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


class TestLoginInteractor:
    def test_invalid_username_return_not_found_http_response(self, access_token_dto):
        # Arrange
        username = "anu-nandu"
        password = "anunandu"
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(LoginPresenterInterface)
        oauth_storage = mock.create_autospec(OAuth2SQLStorage)
        interactor = LoginInteractor(storage=storage, oauth_storage=oauth_storage)
        from auth_app.exceptions.common_exceptions import InvalidUsername
        storage.validate_user_name.side_effect = InvalidUsername
        mock_obj = mock.Mock()
        presenter.get_username_not_found_http_response.return_value = mock_obj

        # Act
        response = interactor.login_wrapper(
            username=username, password=password, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        storage.validate_user_name. \
            assert_called_once_with(username=username)
        presenter.get_username_not_found_http_response.assert_called_once()

    def test_invalid_password_return_not_found_http_response(self):
        # Arrange
        username = "anu-nandu"
        password = "anunandu"
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(LoginPresenterInterface)
        oauth_storage = mock.create_autospec(OAuth2SQLStorage)
        interactor = LoginInteractor(storage=storage, oauth_storage=oauth_storage)
        from auth_app.interactors.login_interactor import InvalidPassword
        storage.valid_password_return_user_id_and_role_dto.side_effect = InvalidPassword
        mock_obj = mock.Mock()
        presenter.get_password_bad_request_http_response.return_value = mock_obj

        # Act
        response = interactor.login_wrapper(
            username=username, password=password, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        storage.valid_password_return_user_id_and_role_dto. \
            assert_called_once_with(username=username, password=password)
        presenter.get_password_bad_request_http_response.assert_called_once()

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_valid_details_return_authuntication_info(self, access_token_dto, user_identity_dto):
        # Arrange
        # print("bsdhsa", access_token_dto)
        username = "anu-nandu"
        password = "anunandu"
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(LoginPresenterInterface)
        oauth_storage = mock.create_autospec(OAuth2SQLStorage)
        interactor = LoginInteractor(storage=storage, oauth_storage=oauth_storage)
        #patch_obj.return_value = access_token_dto
        OAuthUserAuthTokensService.create_user_auth_tokens.return_value = access_token_dto
        storage.valid_password_return_user_id_and_role_dto.return_value = user_identity_dto
        from auth_app.interactors.dtos import AuthenticationDto
        authentication_dto = AuthenticationDto(
            access_token=access_token_dto.access_token,
            is_admin=user_identity_dto.is_admin
        )
        mock_obj = mock.Mock()
        presenter.get_login_response.return_value = mock_obj

        # Act
        response = interactor.login_wrapper(
            username=username, password=password, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        presenter.get_login_response.assert_called_once_with(authentication_dto)


