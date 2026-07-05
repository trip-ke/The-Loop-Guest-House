from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sku = models.CharField(max_length=60, unique=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=5)
    unit = models.CharField(max_length=30, default="pcs")
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    @property
    def needs_restock(self):
        return self.quantity <= self.reorder_level

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    class MovementType(models.TextChoices):
        IN = "in", "Stock In"
        OUT = "out", "Stock Out"
        ADJUSTMENT = "adjustment", "Adjustment"

    item = models.ForeignKey(InventoryItem, on_delete=models.PROTECT, related_name="movements")
    movement_type = models.CharField(max_length=20, choices=MovementType.choices)
    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.item}"

# Create your models here.
