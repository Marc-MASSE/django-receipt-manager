import unittest
from django.test import TestCase as DjangoTestCase
from django.urls import reverse

from receiptapp.forms import ReceiptForm
from receiptapp.models import Receipt


class TestViews(DjangoTestCase):

    def setUp(self):
        self.receipt1 = Receipt.objects.create(
            date="2001-01-01",
            title="Receipt1",
            amount=100.00
        )
        self.receipt2 = Receipt.objects.create(
            date="2002-02-02",
            title="Receipt2",
            amount=200.00
        )

    def test_welcome_view(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/welcome.html')

    def test_receipt_list_view(self):
        response = self.client.get(reverse('receipt-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/receipt_list.html')
        self.assertContains(response, self.receipt1.title)
        self.assertContains(response, self.receipt2.title)

    def test_receipt_detail_view(self):
        response = self.client.get(reverse('receipt-detail', args=[self.receipt1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/receipt_detail.html')
        self.assertContains(response, self.receipt1.title)

    def test_receipt_create_view(self):
        url = reverse('receipt-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/receipt_create.html')
        self.assertIsInstance(response.context['form'], ReceiptForm)

    def test_receipt_create_post(self):
        url = reverse('receipt-create')
        data = {
            'title': 'New Receipt',
            'amount': 300.00,
            'date': '2023-09-28',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirection after creation

        # To ensure the receipt was created in the database
        self.assertTrue(Receipt.objects.filter(title='New Receipt').exists())

    def test_receipt_update_view(self):
        url = reverse('receipt-update', args=[self.receipt1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/receipt_update.html')
        self.assertIsInstance(response.context['form'], ReceiptForm)

    def test_receipt_update_post(self):
        url = reverse('receipt-update', args=[self.receipt1.id])
        updated_data = {
            'title': 'Updated Receipt',
            'amount': 400.00,
            'date': '2023-09-29',
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)  # Redirection after update

        # To ensure the receipt was updated in the database
        self.receipt1.refresh_from_db()
        self.assertEqual(self.receipt1.title, 'Updated Receipt')

    def test_receipt_delete_view(self):
        url = reverse('receipt-delete', args=[self.receipt1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receiptapp/receipt_delete.html')

    def test_receipt_delete_post(self):
        url = reverse('receipt-delete', args=[self.receipt1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirection after delete

        # To ensure the receipt has been deleted from the database
        self.assertFalse(Receipt.objects.filter(title='Receipt1').exists())


if __name__ == '__main__':
    unittest.main()
