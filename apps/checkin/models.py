from django.conf import settings
from django.db import models
from django.utils import timezone


class CheckIn(models.Model):
    reservation = models.OneToOneField(
        "reservations.Reservation",
        on_delete=models.PROTECT,
        related_name="checkin_record",
    )
    checked_in_at = models.DateTimeField(default=timezone.now)
    checked_in_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="checkins",
    )
    key_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-checked_in_at"]

    def __str__(self):
        return f"Check-in for {self.reservation}"

# Create your models here.
