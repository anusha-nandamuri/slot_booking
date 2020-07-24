import datetime

import factory
from factory.fuzzy import FuzzyDate

from slot_booking.models import UserSlot, WashingMachine, Slot


class SlotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Slot

    day = factory.Iterator(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    start_time = factory.Iterator([datetime.time(hour=9), datetime.time(hour=10)])
    end_time = factory.Iterator([datetime.time(hour=10), datetime.time(hour=11)])


class WashingMachineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WashingMachine

    id = factory.Sequence(lambda a: f'Washing_machine_{a}')


class UserSlotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserSlot

    user_id = factory.Sequence(lambda a: a)
    slot = factory.SubFactory(Slot)
    date = FuzzyDate(start_date=datetime.date(2020, 7, 21), end_date=datetime.date(2020, 7, 26))
    start_time = factory.Iterator([datetime.time(hour=9), datetime.time(hour=10)])
    end_time = factory.Iterator([datetime.time(hour=10), datetime.time(hour=11)])
    washing_machine = factory.Iterator([WashingMachine.objects.all()])
