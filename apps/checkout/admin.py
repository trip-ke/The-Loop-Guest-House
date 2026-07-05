from django.contrib import admin

from .models import CheckOut


@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ("checkin", "checked_out_at", "checked_out_by", "total_due")
    search_fields = ("checkin__reservation__guest__first_name", "checkin__reservation__guest__last_name")
    date_hierarchy = "checked_out_at"

# Register your models here.
