from django.conf import settings
from django.db import models
from django.utils import timezone


class CheckOut(models.Model):
    checkin = models.OneToOneField(
        "checkin.CheckIn",
        on_delete=models.PROTECT,
        related_name="checkout_record",
    )
    checked_out_at = models.DateTimeField(default=timezone.now)
    checked_out_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="checkouts",
    )
    room_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    @property
    def total_due(self):
        return self.room_charges + self.extra_charges - self.discount

    def __str__(self):
        return f"Check-out for {self.checkin.reservation}"

# Create your models here.
