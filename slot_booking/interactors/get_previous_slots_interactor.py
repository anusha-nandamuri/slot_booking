from typing import List

from django.http import HttpResponse

from slot_booking.interactors.presenters.presenter_interface import PreviousSlotsPresenterInterface
from slot_booking.exceptions.exceptions import InvalidLimitValue, InvalidOffsetValue
from slot_booking.interactors.storages.dtos import CompleteSlotDetailsDto
from slot_booking.interactors.storages.storage_interface import StorageInterface


class GetPreviousSlotsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_previous_slots_wrapper(
            self, user_id: int, limit: int,
            offset: int, presenter: PreviousSlotsPresenterInterface
    ) -> HttpResponse:
        try:
            previous_slots_dtos = self.get_previous_slots_interactor(
                user_id=user_id, limit=limit, offset=offset
            )
        except InvalidLimitValue as error_obj:
            http_response = presenter.get_limit_bad_request_response(error_obj)
            return http_response
        except InvalidOffsetValue as error_obj:
            http_response = presenter.get_offset_bad_request_response(error_obj)
            return http_response
        http_response = presenter.get_previous_slots_response(previous_slots_dtos=previous_slots_dtos)
        return http_response

    def get_previous_slots_interactor(self, user_id: int, limit: int, offset: int) -> List[CompleteSlotDetailsDto]:
        is_limit_negative = self._check_is_negative_value(number=limit)
        if is_limit_negative:
            raise InvalidLimitValue(invalid_limit_value=limit)
        is_offset_negative = self._check_is_negative_value(number=offset)
        if is_offset_negative:
            raise InvalidOffsetValue(invalid_offset_value=offset)
        previous_slot_ids = self.storage.get_previous_slots_ids(user_id=user_id)
        previous_slot_ids_with_applied_limit_and_offset = previous_slot_ids[offset: offset + limit]
        previous_slots_dtos = self.storage.get_slots_details(slot_ids=previous_slot_ids_with_applied_limit_and_offset)
        return previous_slots_dtos



    @staticmethod
    def _check_is_negative_value(number: int):
        if number < 0:
            return True
        return False
