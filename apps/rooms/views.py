from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RoomForm, RoomTypeForm
from .models import Room, RoomType


class RoomListView(LoginRequiredMixin, ListView):
    model = Room
    paginate_by = 10
    template_name = "rooms/room_list.html"

    def get_queryset(self):
        queryset = Room.objects.select_related("room_type")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(number__icontains=query)
                | Q(floor__icontains=query)
                | Q(room_type__name__icontains=query)
            )
        return queryset


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = "form.html"
    success_url = reverse_lazy("rooms:list")


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    form_class = RoomForm
    template_name = "form.html"
    success_url = reverse_lazy("rooms:list")


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("rooms:list")


class RoomTypeListView(LoginRequiredMixin, ListView):
    model = RoomType
    template_name = "rooms/room_type_list.html"


class RoomTypeCreateView(LoginRequiredMixin, CreateView):
    model = RoomType
    form_class = RoomTypeForm
    template_name = "form.html"
    success_url = reverse_lazy("rooms:type-list")

# Create your views here.
