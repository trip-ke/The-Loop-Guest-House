from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ReservationForm
from .models import Reservation


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    paginate_by = 10
    template_name = "reservations/reservation_list.html"

    def get_queryset(self):
        queryset = Reservation.objects.select_related("guest", "room")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(guest__first_name__icontains=query)
                | Q(guest__last_name__icontains=query)
                | Q(room__number__icontains=query)
                | Q(status__icontains=query)
            )
        return queryset


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "form.html"
    success_url = reverse_lazy("reservations:list")


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "form.html"
    success_url = reverse_lazy("reservations:list")


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("reservations:list")

# Create your views here.
