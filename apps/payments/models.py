from django.db import models


class Payment(models.Model):
    class Method(models.TextChoices):
        CASH = "cash", "Cash"
        CARD = "card", "Card"
        MPESA = "mpesa", "M-Pesa"
        BANK = "bank", "Bank Transfer"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"
        REFUNDED = "refunded", "Refunded"

    reservation = models.ForeignKey("reservations.Reservation", on_delete=models.PROTECT, related_name="payments")
    method = models.CharField(max_length=20, choices=Method.choices, default=Method.CASH)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.COMPLETED)
    transaction_reference = models.CharField(max_length=120, blank=True)
    paid_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-paid_at"]

    def __str__(self):
        return f"{self.get_method_display()} payment of {self.amount}"

# Create your models here.
