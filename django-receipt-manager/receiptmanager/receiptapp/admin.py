from django.contrib import admin

from receiptapp.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'amount')


admin.site.register(Receipt, ReceiptAdmin)
