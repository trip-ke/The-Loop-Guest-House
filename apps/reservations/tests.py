from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.guests.models import Guest
from apps.reservations.models import Reservation
from apps.rooms.models import Room, RoomType


class ReservationModelTests(TestCase):
    def setUp(self):
        room_type = RoomType.objects.create(name="Standard", base_price=3500, capacity=2)
        self.room = Room.objects.create(number="101", room_type=room_type)
        self.guest = Guest.objects.create(first_name="Test", last_name="Guest", phone="0700000000")

    def test_rejects_checkout_before_checkin(self):
        reservation = Reservation(
            guest=self.guest,
            room=self.room,
            check_in_date=date(2026, 7, 10),
            check_out_date=date(2026, 7, 10),
            rate=3500,
        )

        with self.assertRaises(ValidationError):
            reservation.full_clean()

    def test_rejects_overlapping_room_booking(self):
        Reservation.objects.create(
            guest=self.guest,
            room=self.room,
            check_in_date=date(2026, 7, 10),
            check_out_date=date(2026, 7, 12),
            rate=3500,
        )
        overlapping = Reservation(
            guest=self.guest,
            room=self.room,
            check_in_date=date(2026, 7, 11),
            check_out_date=date(2026, 7, 13),
            rate=3500,
        )

        with self.assertRaises(ValidationError):
            overlapping.full_clean()

    def test_allows_back_to_back_booking(self):
        Reservation.objects.create(
            guest=self.guest,
            room=self.room,
            check_in_date=date(2026, 7, 10),
            check_out_date=date(2026, 7, 12),
            rate=3500,
        )
        next_booking = Reservation(
            guest=self.guest,
            room=self.room,
            check_in_date=date(2026, 7, 12),
            check_out_date=date(2026, 7, 14),
            rate=3500,
        )

        next_booking.full_clean()
