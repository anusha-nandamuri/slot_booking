from django.db import models

from slot_booking.constants.enums import Day


class Slot(models.Model):
    day_choices = Day.get_list_of_tuples()
    day = models.DateField(choices=day_choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time}-{self.end_time}"
