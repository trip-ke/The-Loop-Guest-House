from django.contrib import admin

from .models import Room, RoomType


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "base_price", "capacity")
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "room_type", "floor", "status", "active")
    list_filter = ("status", "room_type", "active")
    search_fields = ("number", "floor")

# Register your models here.
