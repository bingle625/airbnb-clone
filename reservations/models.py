from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """Reservation model definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "cancled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCLED, "Cancled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self. check_out
    
    is_finished.boolean = True