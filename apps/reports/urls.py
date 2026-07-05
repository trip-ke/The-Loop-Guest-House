from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [
    path("reservations.pdf", views.reservations_pdf, name="reservations-pdf"),
    path("reservations.xlsx", views.reservations_excel, name="reservations-excel"),
]
