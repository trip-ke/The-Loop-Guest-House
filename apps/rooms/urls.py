from django.urls import path

from . import views

app_name = "rooms"

urlpatterns = [
    path("", views.RoomListView.as_view(), name="list"),
    path("new/", views.RoomCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.RoomUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.RoomDeleteView.as_view(), name="delete"),
    path("types/", views.RoomTypeListView.as_view(), name="type-list"),
    path("types/new/", views.RoomTypeCreateView.as_view(), name="type-create"),
]
