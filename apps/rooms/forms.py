from django import forms

from .models import Room, RoomType


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ["name", "description", "base_price", "capacity"]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["number", "room_type", "floor", "status", "notes", "active"]
