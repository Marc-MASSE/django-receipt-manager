from django.contrib import admin
from django.urls import path
from receiptapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='welcome'),
    path('receipts/', views.receipt_list, name='receipt-list'),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt-detail'),
    path('receipt/create/', views.receipt_create, name='receipt-create'),
    path('receipt/<int:receipt_id>/update', views.receipt_update, name='receipt-update')
]
