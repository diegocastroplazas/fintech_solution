from django.db import models
from loans.data import STATUS_CHOICES


class Loan(models.Model):
    """Loan model"""

    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=60, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)
    contract_version = models.CharField(max_length=30)
    maximum_payment_date = models.DateTimeField()
    taken_at = models.DateTimeField()
    outstanding_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "loans"
        ordering = ["id"]
