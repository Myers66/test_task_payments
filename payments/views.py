from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from .models import Payment, Client

def index(request):
    return render(request, 'payments/index.html')

def api_data(request):
    payments = Payment.objects.select_related('payer').order_by('pay_date')
    line_data = [{'date': p.pay_date.isoformat(), 'amount': float(p.amount)} for p in payments]

    clients_totals = Client.objects.annotate(total_amount=Sum('payments__amount')).filter(total_amount__isnull=False)
    bar_data = [{'client_name': f"{c.first_name} {c.last_name}", 'total_amount': float(c.total_amount)} for c in clients_totals]

    return JsonResponse({'line_data': line_data, 'bar_data': bar_data})