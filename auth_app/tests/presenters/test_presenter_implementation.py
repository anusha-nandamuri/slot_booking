import pytest
from auth_app.presenters.presenter_implementation import LoginPresenterImplementation, SignupPresenterImplementation


class Testlogin:
    def test_get_login_response_returns_user_authentications_details_dto(self, snapshot):
        # Arrange
        from auth_app.interactors.storages.dtos import UserIdentityDto
        from auth_app.interactors.dtos import AuthenticationDto
        authentication_details = AuthenticationDto(
            access_token="mytoken",
            is_admin=True
        )
        presenter = LoginPresenterImplementation()

        # Act
        login_success_response = presenter.get_login_response(authentication_details)

        # Assert
        snapshot.assert_match(login_success_response, 'http_response')

    def test_get_username_not_found_http_response(self, snapshot):
        # Arrange
        presenter = LoginPresenterImplementation()

        # Act
        response = presenter.get_username_not_found_http_response()

        # Assert
        snapshot.assert_match(response, 'http_response')

    def test_get_password_bad_request_http_response(self, snapshot):
        # Arrange
        presenter = LoginPresenterImplementation()

        # Act
        response = presenter.get_password_bad_request_http_response()

        # Assert
        snapshot.assert_match(response, 'http_response')


class TestSignup:
    def test_get_user_name_already_exist_bad_request_response(self, snapshot):
        # Arrange
        presenter = SignupPresenterImplementation()

        # Act
        response = presenter.get_user_name_already_exist_bad_request_response()

        # Assert
        snapshot.assert_match(response, 'http_response')

    def test_get_signup_success_responce(self, snapshot):
        # Arrange
        presenter = SignupPresenterImplementation()

        # Act
        response = presenter.get_signup_success_responce()

        # Assert
        snapshot.assert_match(response, 'http_response')