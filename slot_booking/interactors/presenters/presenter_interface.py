import abc
from typing import List

from django.http import HttpResponse

from slot_booking.exceptions.exceptions import InvalidLimitValue, InvalidOffsetValue
from slot_booking.interactors.storages.dtos import AvailableSlotsDto, CompleteSlotDetailsDto


class AvailableSlotsPresenterInterface:
    @abc.abstractmethod
    def get_available_slots_response(
            self, available_slots_dto: List[AvailableSlotsDto]
    ) -> HttpResponse:
        pass


class UpcomingSlotsPresenterInterface:
    @abc.abstractmethod
    def get_upcoming_slots_response(
            self, upcoming_slots_dto: List[CompleteSlotDetailsDto]
    ) -> HttpResponse:
        pass


class PreviousSlotsPresenterInterface:
    @abc.abstractmethod
    def get_limit_bad_request_response(self, error_obj: InvalidLimitValue) -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_offset_bad_request_response(self, error_obj: InvalidOffsetValue) -> HttpResponse:
        pass

    @abc.abstractmethod
    def get_previous_slots_response(self, previous_slots_dtos: List[CompleteSlotDetailsDto]) -> HttpResponse:
        pass
