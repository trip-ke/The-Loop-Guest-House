from django.contrib import admin

from .models import Invoice, InvoiceLine


class InvoiceLineInline(admin.TabularInline):
    model = InvoiceLine
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceLineInline]
    list_display = ("invoice_number", "reservation", "status", "tax_rate", "created_at")
    list_filter = ("status",)
    search_fields = ("invoice_number", "reservation__guest__first_name", "reservation__guest__last_name")

# Register your models here.
