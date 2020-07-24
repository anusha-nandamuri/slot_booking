import pytest

from slot_booking.tests.factories.models import WashingMachineFactory, UserSlotFactory, SlotFactory


@pytest.fixture
def create_slots():
    SlotFactory.create_batch(14)


@pytest.fixture
def create_washing_machine():
    WashingMachineFactory.create_batch(3)


@pytest.fixture
def create_slots_for_user():
    UserSlotFactory.create_batch(4)
