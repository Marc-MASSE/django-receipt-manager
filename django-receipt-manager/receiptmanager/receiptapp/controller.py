
class Controller:
    def __init__(self, receipts):
        self.receipts = receipts

    def totals_per_month(self):
        """
        Method for calculating totals per month.
        :returns: a list of tuples where the first element is the month (in YYYY-MM format)
                    and the second element is the corresponding sum.
        """
        totals = {}
        for receipt in self.receipts:
            month = receipt.date.strftime('%Y-%m')
            if month in totals:
                totals[month] += receipt.amount
            else:
                totals[month] = receipt.amount

        # To convert dictionary to a list of tuples
        result = [(month, total) for month, total in totals.items()]
        return result

    def grand_total(self):
        """
        :return: the sum of all amounts.
        """
        total = sum(receipt.amount for receipt in self.receipts)
        return total
