# TODO: get available slots
import datetime
from unittest import mock

from freezegun import freeze_time

from slot_booking.interactors.storages.storage_interface import StorageInterface


@freeze_time('2020-7-23')
def test_get_available_slots_return_available_slots_response(available_slot_dto):
    # Arrange
    user_id = 1
    bookable_dates = [
        datetime.date(2020, 7, 23),
        datetime.date(2020, 7, 24),
        datetime.date(2020, 7, 25)
    ]
    storage = mock.create_autospec(StorageInterface)
    from slot_booking.interactors.presenters.presenter_interface import\
        AvailableSlotsPresenterInterface
    presenter = mock.create_autospec(AvailableSlotsPresenterInterface)
    from slot_booking.interactors.get_available_slots_interactor import GetAvailableSlotsInteractor
    interactor = GetAvailableSlotsInteractor(storage=storage)
    storage.get_available_slot_details.return_value = available_slot_dto
    mock_obj = mock.Mock()
    presenter.get_available_slots_response.return_value = mock_obj

    # Act
    response = interactor.get_available_slots_wrapper(user_id=user_id, presenter=presenter)

    # Assert
    assert response == mock_obj
    storage.get_available_slot_details.assert_called_once_with(
        user_id=user_id, bookable_dates=bookable_dates
    )
    presenter.get_available_slots_response.assert_called_once_with(available_slot_dto)
