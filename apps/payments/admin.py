from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("reservation", "method", "amount", "status", "transaction_reference", "paid_at")
    list_filter = ("method", "status")
    search_fields = ("transaction_reference", "reservation__guest__first_name", "reservation__guest__last_name")
    date_hierarchy = "paid_at"

# Register your models here.
