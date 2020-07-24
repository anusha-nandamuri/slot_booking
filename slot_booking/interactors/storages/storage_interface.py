import abc
import datetime
from typing import List

from slot_booking.interactors.storages.dtos import AvailableSlotsDto


class StorageInterface:
    @abc.abstractmethod
    def get_available_slot_details(self, user_id: int, bookable_dates: List[datetime.date]) -> List[AvailableSlotsDto]:
        pass

    @abc.abstractmethod
    def get_upcoming_slot_ids(self, user_id: int):
        pass

    @abc.abstractmethod
    def get_slots_details(self, slot_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_previous_slots_ids(self, user_id: int):
        pass
