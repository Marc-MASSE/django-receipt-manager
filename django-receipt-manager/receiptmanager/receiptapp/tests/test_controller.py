import unittest
from datetime import datetime

from receiptapp.controller import Controller
from receiptapp.models import Receipt


class TestController(unittest.TestCase):
    def setUp(self):
        self.receipts = [
            Receipt(date=datetime(2023, 1, 5), title="Receipt 1", amount=100.0),
            Receipt(date=datetime(2023, 1, 10), title="Receipt 2", amount=200.0),
            Receipt(date=datetime(2023, 2, 15), title="Receipt 3", amount=150.0),
            Receipt(date=datetime(2023, 3, 20), title="Receipt 4", amount=300.0),
        ]

    def test_totals_per_month(self):
        controller = Controller(self.receipts)
        expected_result = [('2023-01', 300.0), ('2023-02', 150.0), ('2023-03', 300.0)]
        self.assertEqual(controller.totals_per_month(), expected_result)

    def test_empty_database_totals_per_month(self):
        controller = Controller([])
        self.assertEqual(controller.totals_per_month(), [])

    def test_grand_total(self):
        controller = Controller(self.receipts)
        expected_result = 750.0
        self.assertEqual(controller.grand_total(), expected_result)


def test_empty_database_grand_total(self):
    controller = Controller([])
    self.assertEqual(controller.grand_total(), 0.0)


if __name__ == '__main__':
    unittest.main()
