from django.conf import settings
from django.db import models


class StaffProfile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        RECEPTIONIST = "receptionist", "Receptionist"
        HOUSEKEEPING = "housekeeping", "Housekeeping"
        ACCOUNTANT = "accountant", "Accountant"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=Role.choices, default=Role.RECEPTIONIST)
    phone = models.CharField(max_length=30, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_role_display()}"

# Create your models here.
