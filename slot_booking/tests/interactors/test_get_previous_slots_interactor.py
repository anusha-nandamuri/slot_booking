from unittest import mock, TestCase

from slot_booking.interactors.get_previous_slots_interactor import GetPreviousSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import PreviousSlotsPresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface


class TestGetPreviousSlotsInteractor:
    def test_invalid_limit_value_limit_bad_request_response(self):
        # Arrange
        user_id = 1
        limit = -3
        offset = 0
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(PreviousSlotsPresenterInterface)
        interactor = GetPreviousSlotsInteractor(storage=storage)
        mock_obj = mock.Mock()
        presenter.get_limit_bad_request_response.return_value = mock_obj

        # Act
        response = interactor.get_previous_slots_wrapper(
            user_id=user_id, limit=limit,
            offset=offset, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        presenter.get_limit_bad_request_response.assert_called_once()

    def test_invalid_offset_value_offset_bad_request_response(self):
        # Arrange
        user_id = 1
        limit = 3
        offset = -1
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(PreviousSlotsPresenterInterface)
        interactor = GetPreviousSlotsInteractor(storage=storage)
        mock_obj = mock.Mock()
        presenter.get_offset_bad_request_response.return_value = mock_obj

        # Act
        response = interactor.get_previous_slots_wrapper(
            user_id=user_id, limit=limit,
            offset=offset, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        presenter.get_offset_bad_request_response.assert_called_once()

    def test_valid_values_return_previous_slots_http_response(self, complete_slot_details_dto):
        # Arrange
        user_id = 1
        limit = 3
        offset = 0
        previous_slot_ids = [1, 2, 3]
        storage = mock.create_autospec(StorageInterface)
        presenter = mock.create_autospec(PreviousSlotsPresenterInterface)
        interactor = GetPreviousSlotsInteractor(storage=storage)
        mock_obj = mock.Mock()
        storage.get_previous_slots_ids.return_value = previous_slot_ids
        storage.get_slots_details.return_value = complete_slot_details_dto
        presenter.get_previous_slots_response.return_value = mock_obj

        # Act
        response = interactor.get_previous_slots_wrapper(
            user_id=user_id, limit=limit,
            offset=offset, presenter=presenter
        )

        # Assert
        assert mock_obj == response
        storage.get_previous_slots_ids.assert_called_once_with(user_id=user_id)
        presenter.get_previous_slots_response.assert_called_once_with(complete_slot_details_dto)



