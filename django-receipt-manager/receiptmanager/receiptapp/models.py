from django.db import models


class Receipt(models.Model):
    """
    A receipt objet contains :
    - a date that must be unique
    - a title limited to 100 characters
    - an amount containing no more than 10 characters and limited to 2 digits after the decimal point
    """
    date = models.DateField(unique=True)
    title = models.fields.CharField(max_length=100)
    amount = models.fields.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()


