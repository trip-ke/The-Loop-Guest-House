from django.urls import path

from . import views

app_name = "reservations"

urlpatterns = [
    path("", views.ReservationListView.as_view(), name="list"),
    path("new/", views.ReservationCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.ReservationUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ReservationDeleteView.as_view(), name="delete"),
]
