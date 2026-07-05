from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["reservation", "method", "amount", "status", "transaction_reference", "notes"]
