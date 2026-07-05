from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render

from apps.guests.models import Guest
from apps.inventory.models import InventoryItem
from apps.payments.models import Payment
from apps.reservations.models import Reservation
from apps.rooms.models import Room


@login_required
def home(request):
    context = {
        "guest_count": Guest.objects.count(),
        "room_count": Room.objects.count(),
        "active_reservations": Reservation.objects.exclude(
            status__in=[Reservation.Status.CANCELLED, Reservation.Status.CHECKED_OUT]
        ).count(),
        "payments_total": Payment.objects.filter(status=Payment.Status.COMPLETED).aggregate(
            total=Sum("amount")
        )["total"]
        or 0,
        "rooms": Room.objects.select_related("room_type")[:8],
        "recent_reservations": Reservation.objects.select_related("guest", "room")[:8],
        "restock_items": InventoryItem.objects.filter(quantity__lte=F("reorder_level"))[:8],
    }
    return render(request, "dashboard/home.html", context)

# Create your views here.
