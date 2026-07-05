from django.contrib import admin

from .models import CheckIn


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ("reservation", "checked_in_at", "checked_in_by", "key_deposit")
    search_fields = ("reservation__guest__first_name", "reservation__guest__last_name", "reservation__room__number")
    date_hierarchy = "checked_in_at"

# Register your models here.
