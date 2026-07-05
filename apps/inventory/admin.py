from django.contrib import admin

from .models import InventoryItem, StockMovement


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "quantity", "reorder_level", "unit", "needs_restock", "active")
    list_filter = ("active",)
    search_fields = ("name", "sku")


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ("item", "movement_type", "quantity", "reason", "created_at")
    list_filter = ("movement_type",)
    search_fields = ("item__name", "reason")

# Register your models here.
