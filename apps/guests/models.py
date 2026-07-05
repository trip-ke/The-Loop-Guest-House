from django.db import models


class Guest(models.Model):
    class IdType(models.TextChoices):
        NATIONAL_ID = "national_id", "National ID"
        PASSPORT = "passport", "Passport"
        DRIVER_LICENSE = "driver_license", "Driver License"
        OTHER = "other", "Other"

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30)
    nationality = models.CharField(max_length=80, blank=True)
    id_type = models.CharField(max_length=30, choices=IdType.choices, default=IdType.NATIONAL_ID)
    id_number = models.CharField(max_length=80, blank=True)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.full_name

# Create your models here.
