import datetime

import factory
from factory.fuzzy import FuzzyDate

from slot_booking.interactors.storages.dtos import AvailableSlotsDto, CompleteSlotDetailsDto


class AvailableSlotsDtoFactory(factory.Factory):
    class Meta:
        model = AvailableSlotsDto

    slot_id = factory.sequence(lambda a: a)
    date = FuzzyDate(start_date=datetime.date(2020, 7, 23), end_date=datetime.date(2020, 7, 26))
    start_time = factory.Iterator([datetime.time(hour=9), datetime.time(hour=10), datetime.time(hour=11)])
    end_time = factory.Iterator([datetime.time(hour=10), datetime.time(hour=11), datetime.time(hour=12)])
    is_available = factory.Iterator([True, False])


class CompleteSlotDetailsDtoFactory(factory.Factory):
    class Meta:
        model = CompleteSlotDetailsDto

    slot_id = factory.sequence(lambda a: a)
    washing_machine_id = factory.sequence(lambda a: a)
    date = FuzzyDate(start_date=datetime.date(2020, 7, 23), end_date=datetime.date(2020, 7, 26))
    start_time = factory.Iterator([datetime.time(hour=9), datetime.time(hour=10), datetime.time(hour=11)])
    end_time = factory.Iterator([datetime.time(hour=10), datetime.time(hour=11), datetime.time(hour=12)])