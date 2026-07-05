from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import GuestForm
from .models import Guest


class GuestListView(LoginRequiredMixin, ListView):
    model = Guest
    paginate_by = 10
    template_name = "guests/guest_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(phone__icontains=query)
                | Q(email__icontains=query)
            )
        return queryset


class GuestDetailView(LoginRequiredMixin, DetailView):
    model = Guest
    template_name = "guests/guest_detail.html"


class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Guest
    form_class = GuestForm
    template_name = "form.html"
    success_url = reverse_lazy("guests:list")


class GuestUpdateView(LoginRequiredMixin, UpdateView):
    model = Guest
    form_class = GuestForm
    template_name = "form.html"
    success_url = reverse_lazy("guests:list")


class GuestDeleteView(LoginRequiredMixin, DeleteView):
    model = Guest
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("guests:list")

# Create your views here.
