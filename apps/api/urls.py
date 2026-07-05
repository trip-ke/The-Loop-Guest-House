from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GuestViewSet, ReservationViewSet, RoomTypeViewSet, RoomViewSet

app_name = "api"

router = DefaultRouter()
router.register("guests", GuestViewSet)
router.register("room-types", RoomTypeViewSet)
router.register("rooms", RoomViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
