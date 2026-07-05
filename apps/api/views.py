from rest_framework.viewsets import ModelViewSet

from apps.guests.models import Guest
from apps.reservations.models import Reservation
from apps.rooms.models import Room, RoomType

from .serializers import GuestSerializer, ReservationSerializer, RoomSerializer, RoomTypeSerializer


class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class RoomTypeViewSet(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.select_related("room_type")
    serializer_class = RoomSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.select_related("guest", "room")
    serializer_class = ReservationSerializer

# Create your views here.
