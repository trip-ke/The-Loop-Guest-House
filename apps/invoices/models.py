from django.db import models


class Invoice(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ISSUED = "issued", "Issued"
        PAID = "paid", "Paid"
        VOID = "void", "Void"

    reservation = models.OneToOneField("reservations.Reservation", on_delete=models.PROTECT, related_name="invoice")
    invoice_number = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    issued_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def subtotal(self):
        return sum(line.line_total for line in self.lines.all())

    @property
    def tax_amount(self):
        return self.subtotal * self.tax_rate / 100

    @property
    def total(self):
        return self.subtotal + self.tax_amount

    def __str__(self):
        return self.invoice_number


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="lines")
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.description

# Create your models here.
