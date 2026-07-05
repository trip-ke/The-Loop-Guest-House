from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import PaymentForm
from .models import Payment


class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    paginate_by = 10
    template_name = "payments/payment_list.html"

    def get_queryset(self):
        return Payment.objects.select_related("reservation", "reservation__guest", "reservation__room")


class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = "form.html"
    success_url = reverse_lazy("payments:list")

# Create your views here.
