from django.db import models


class Receipt(models.Model):
    date = models.DateField(unique=True)
    title = models.fields.CharField(max_length=100)
    amount = models.fields.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()


