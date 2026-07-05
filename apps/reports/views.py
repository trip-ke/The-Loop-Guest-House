from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas

from apps.reservations.models import Reservation


@login_required
def reservations_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="reservations.pdf"'

    pdf = canvas.Canvas(response)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, 800, "Loop Guest House Reservations")
    pdf.setFont("Helvetica", 10)

    y = 760
    for reservation in Reservation.objects.select_related("guest", "room")[:40]:
        line = (
            f"{reservation.guest.full_name} | Room {reservation.room.number} | "
            f"{reservation.check_in_date} to {reservation.check_out_date} | {reservation.status}"
        )
        pdf.drawString(40, y, line)
        y -= 18
        if y < 60:
            pdf.showPage()
            y = 800

    pdf.save()
    return response


@login_required
def reservations_excel(request):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Reservations"
    sheet.append(["Guest", "Room", "Check In", "Check Out", "Status", "Rate", "Total"])

    for reservation in Reservation.objects.select_related("guest", "room"):
        sheet.append(
            [
                reservation.guest.full_name,
                reservation.room.number,
                reservation.check_in_date,
                reservation.check_out_date,
                reservation.get_status_display(),
                reservation.rate,
                reservation.total_amount,
            ]
        )

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="reservations.xlsx"'
    workbook.save(response)
    return response

# Create your views here.
