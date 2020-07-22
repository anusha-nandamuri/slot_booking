from unittest import mock

from auth_app.interactors.presenters.presenter_interface import SignupPresenterInterface
from auth_app.interactors.signup_interactor import SignupInteractor
from auth_app.interactors.storages.storage_interface import StorageInterface


class TestSignupInteractor:
    def test_existing_username_bad_request_http_response(self):
        # Arrange
        username = "user1"
        password = "password1"
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(SignupPresenterInterface)
        interactor = SignupInteractor(storage=storage)
        storage.validate_user_name.return_value = None
        mock_obj = mock.Mock()
        presenter.get_user_name_already_exist_bad_request_response.return_value = mock_obj

        # Act
        return_value = interactor.signup_wrapper(username=username, password=password, presenter=presenter)

        # Assert
        assert mock_obj == return_value
        storage.validate_user_name.assert_called_once_with(username)
        presenter.get_user_name_already_exist_bad_request_response.assert_called_once()

    def test_creates_user_return_success_response(self):
        # Arrange
        username = "user1"
        password = "password1"
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(SignupPresenterInterface)
        interactor = SignupInteractor(storage=storage)
        from auth_app.exceptions.common_exceptions import InvalidUsername
        storage.validate_user_name.side_effect = InvalidUsername
        mock_obj = mock.Mock()
        presenter.get_signup_success_responce.return_value = mock_obj

        # Act
        return_value = interactor.signup_wrapper(username=username, password=password, presenter=presenter)

        # Assert
        assert mock_obj == return_value
        storage.validate_user_name.assert_called_once_with(username)
        storage.signup_user.assert_called_once_with(username=username, password=password)
        presenter.get_signup_success_responce.assert_called_once()




