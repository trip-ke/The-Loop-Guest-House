from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("guest", "room", "check_in_date", "check_out_date", "status", "rate")
    list_filter = ("status", "check_in_date", "room__room_type")
    search_fields = ("guest__first_name", "guest__last_name", "room__number")
    date_hierarchy = "check_in_date"

# Register your models here.
