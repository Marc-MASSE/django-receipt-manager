from django.shortcuts import render

from receiptapp.models import Receipt


def welcome(request):
    return render(request, 'receiptapp/welcome.html')


def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(
        request,
        'receiptapp/receipt_list.html',
        {'receipts': receipts}
    )

