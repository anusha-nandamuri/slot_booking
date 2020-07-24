from django.db import models

from slot_booking.models import Slot
from slot_booking.models.washing_machine import WashingMachine


class UserSlot(models.Model):
    user_id = models.IntegerField()
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, related_name="booked_slot_details")
    date = models.DateField(auto_now=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    washing_machine = models.ForeignKey(to=WashingMachine, on_delete=models.SET_NULL, related_name="slots_given")
