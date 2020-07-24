import datetime
from typing import List

from django.http import HttpResponse

from slot_booking.interactors.presenters.presenter_interface import AvailableSlotsPresenterInterface
from slot_booking.interactors.storages.dtos import AvailableSlotsDto
from slot_booking.interactors.storages.storage_interface import StorageInterface


class GetAvailableSlotsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_available_slots_wrapper(
            self, user_id, presenter: AvailableSlotsPresenterInterface
    ) -> HttpResponse:
        available_slots_dtos = self.get_available_slots_interactor(user_id=user_id)
        http_response = presenter.get_available_slots_response(
            available_slots_dto=available_slots_dtos
        )
        return http_response

    def get_available_slots_interactor(self, user_id: int) -> List[AvailableSlotsDto]:
        today_date = datetime.date.today()
        bookable_dates = []
        from slot_booking.constants.constants import DAYS_COUNT_AVAILABLE_TO_BOOK_A_SLOT
        for one_day in range(DAYS_COUNT_AVAILABLE_TO_BOOK_A_SLOT):
            this_date = today_date + datetime.timedelta(days=one_day)
            bookable_dates.append(this_date)

        available_slots_dto = self.storage.get_available_slot_details(user_id=user_id, bookable_dates=bookable_dates)

        return available_slots_dto
