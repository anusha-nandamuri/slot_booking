from datetime import date

from slot_booking.models import UserSlot


class StorageImplementation(StorageInterface):
    def get_available_slot_details(self, user_id: int, from_date: date, to_date: date):
        available_slots_dto = []
        days = []
        for fr
        user_slots = UserSlot.objects.filter(user_id=user_id, date__gte=from_date, to_date__lt=to_date)
        for slot in user_slots:
            available_slots_dto.append(
                AvailableSlotsDto(
                    slot_id=slot.

                )
            )