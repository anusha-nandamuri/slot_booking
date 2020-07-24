import pytest

from slot_booking.tests.factories.interactor_dtos import AvailableSlotsDtoFactory, CompleteSlotDetailsDtoFactory


@pytest.fixture
def available_slot_dto():
    available_slot_dtos = AvailableSlotsDtoFactory.create_batch(20)
    AvailableSlotsDtoFactory.start_time.reset()
    AvailableSlotsDtoFactory.end_time.reset()
    AvailableSlotsDtoFactory.is_available.reset()
    AvailableSlotsDtoFactory.reset_sequence()
    return available_slot_dtos


@pytest.fixture
def complete_slot_details_dto():
    complete_slot_details_dtos = CompleteSlotDetailsDtoFactory.create_batch(5)
    CompleteSlotDetailsDtoFactory.start_time.reset()
    CompleteSlotDetailsDtoFactory.end_time.reset()
    CompleteSlotDetailsDtoFactory.reset_sequence()
    return complete_slot_details_dtos
