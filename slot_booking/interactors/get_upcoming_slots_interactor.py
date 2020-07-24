from typing import List

from django.http import HttpResponse

from slot_booking.interactors.presenters.presenter_interface import UpcomingSlotsPresenterInterface
from slot_booking.interactors.storages.dtos import CompleteSlotDetailsDto
from slot_booking.interactors.storages.storage_interface import StorageInterface


class GetUpComingSlotsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_upcoming_slots_wrapper(
            self, user_id: int, presenter: UpcomingSlotsPresenterInterface
    ) -> HttpResponse:
        upcoming_slots_dtos = self.get_upcoming_slots_interactor(user_id=user_id)
        http_response = presenter.get_upcoming_slots_response(upcoming_slots_dto=upcoming_slots_dtos)
        return http_response

    def get_upcoming_slots_interactor(self, user_id: int) -> List[CompleteSlotDetailsDto]:
        slot_ids = self.storage.get_upcoming_slot_ids(user_id=user_id)
        upcoming_slots_dtos = self.storage.get_slots_details(slot_ids=slot_ids)
        return upcoming_slots_dtos
