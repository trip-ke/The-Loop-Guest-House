from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "guest",
            "room",
            "check_in_date",
            "check_out_date",
            "adults",
            "children",
            "status",
            "rate",
            "notes",
        ]
        widgets = {
            "check_in_date": forms.DateInput(attrs={"type": "date"}),
            "check_out_date": forms.DateInput(attrs={"type": "date"}),
        }
