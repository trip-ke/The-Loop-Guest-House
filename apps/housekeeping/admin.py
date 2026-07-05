from django.contrib import admin

from .models import HousekeepingTask


@admin.register(HousekeepingTask)
class HousekeepingTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "room", "assigned_to", "status", "due_date")
    list_filter = ("status", "due_date")
    search_fields = ("title", "room__number", "assigned_to__username")

# Register your models here.
