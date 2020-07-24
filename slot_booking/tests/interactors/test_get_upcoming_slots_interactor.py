from unittest import mock

from slot_booking.interactors.get_upcoming_slots_interactor import GetUpComingSlotsInteractor
from slot_booking.interactors.presenters.presenter_interface import UpcomingSlotsPresenterInterface
from slot_booking.interactors.storages.storage_interface import StorageInterface


def test_get_upcoming_slots_return_upconing_slots_response(complete_slot_details_dto):
    # Arrange
    user_id = 1
    upcoming_slot_ids = [1, 2, 3]
    storage = mock.create_autospec(StorageInterface)
    presenter = mock.create_autospec(UpcomingSlotsPresenterInterface)
    interactor = GetUpComingSlotsInteractor(storage=storage)
    storage.get_upcoming_slot_ids.return_value = upcoming_slot_ids
    storage.get_slots_details.return_value = complete_slot_details_dto
    mock_obj = mock.Mock()
    presenter.get_upcoming_slots_response.return_value = mock_obj

    # Act
    response = interactor.get_upcoming_slots_wrapper(user_id=user_id, presenter=presenter)

    # Assert
    assert response == mock_obj
    storage.get_upcoming_slot_ids.assert_called_once_with(user_id=user_id)
    storage.get_slots_details.assert_called_once_with(upcoming_slot_ids)
    presenter.get_upcoming_slots_response.assert_called_once_with(complete_slot_details_dto)
