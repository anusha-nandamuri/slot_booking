from dataclasses import dataclass
from datetime import date, time


@dataclass
class SlotDetailsDto:
    slot_id: int
    date: date
    start_time: time
    end_time: time


@dataclass
class AvailableSlotsDto(SlotDetailsDto):
    is_available: bool

@dataclass
class CompleteSlotDetailsDto(SlotDetailsDto):
    washing_machine_id: int
