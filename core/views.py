import json
from django.http import JsonResponse
from django.shortcuts import render
from qrdata.models import PaymentQR


def home(request):
    return render(request, "home.html")

def checkout(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session["payment_data"] = data
        return JsonResponse({"status": "ok"})

def payment(request):
    data = request.session.get("payment_data")
    qr = PaymentQR.objects.first()   # active QR
    return render(request, "payment.html", {
        "data": data,
        "qr_url": qr.qr_image.url if qr else None
    })
