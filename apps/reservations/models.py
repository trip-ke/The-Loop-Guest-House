from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CHECKED_IN = "checked_in", "Checked In"
        CHECKED_OUT = "checked_out", "Checked Out"
        CANCELLED = "cancelled", "Cancelled"
        NO_SHOW = "no_show", "No Show"

    guest = models.ForeignKey("guests.Guest", on_delete=models.PROTECT, related_name="reservations")
    room = models.ForeignKey("rooms.Room", on_delete=models.PROTECT, related_name="reservations")
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adults = models.PositiveSmallIntegerField(default=1)
    children = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.PENDING)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-check_in_date", "room__number"]

    @property
    def nights(self):
        return max((self.check_out_date - self.check_in_date).days, 0)

    @property
    def total_amount(self):
        return self.rate * self.nights

    def clean(self):
        if self.check_out_date <= self.check_in_date:
            raise ValidationError("Check-out date must be after check-in date.")

        overlapping = Reservation.objects.filter(
            room=self.room,
            check_in_date__lt=self.check_out_date,
            check_out_date__gt=self.check_in_date,
        ).exclude(status__in=[self.Status.CANCELLED, self.Status.NO_SHOW])

        if self.pk:
            overlapping = overlapping.exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This room is already booked for the selected dates.")

    def __str__(self):
        return f"{self.guest} - {self.room} ({self.check_in_date} to {self.check_out_date})"

# Create your models here.
