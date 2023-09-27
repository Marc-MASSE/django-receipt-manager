from django.shortcuts import render, redirect

from receiptapp.forms import ReceiptForm
from receiptapp.models import Receipt


def welcome(request):
    return render(request, 'receiptapp/welcome.html')


def receipt_list(request):
    # The prefix - before the date field means that receipts will be sorted in descending order based on their date.
    receipts = Receipt.objects.all().order_by('-date')
    return render(
        request,
        'receiptapp/receipt_list.html',
        {'receipts': receipts}
    )


def receipt_detail(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)
    return render(
        request,
        'receiptapp/receipt_detail.html',
        {'receipt': receipt}
    )


def receipt_create(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            return redirect('receipt-detail', receipt.id)
    else:
        form = ReceiptForm()
    return render(
        request,
        'receiptapp/receipt_create.html',
        {'form': form}
    )


def receipt_update(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)

    if request.method == 'POST':
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save()
            return redirect('receipt-detail', receipt.id)
    else:
        form = ReceiptForm(instance=receipt)
    return render(
        request,
        'receiptapp/receipt_update.html',
        {'form': form}
    )


def receipt_delete(request, receipt_id):
    receipt = Receipt.objects.get(id=receipt_id)

    if request.method == 'POST':
        receipt.delete()
        return redirect('receipt-list')
    return render(
        request,
        'receiptapp/receipt_delete.html',
        {'receipt': receipt}
    )

