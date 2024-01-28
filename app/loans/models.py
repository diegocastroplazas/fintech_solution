from django.db import models


class Loan(models.Model):
    """Loan model"""

    class Status(models.IntegerChoices):
        PENDING = 1, "Pending"
        ACTIVE = 2, "Active"
        REJECTED = 3, "Rejected"
        PAID = 4, "Paid"

    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=60, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.SmallIntegerField(choices=Status.choices, default=Status.PENDING)
    contract_version = models.CharField(max_length=30)
    maximum_payment_date = models.DateTimeField(blank=True, null=True)
    taken_at = models.DateTimeField(blank=True, null=True)
    outstanding_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)

    @property
    def costumer_external_id(self):
        return self.customer.external_id

    def __str__(self):
        return f"Loan: {self.id} - {self.external_id}"

    class Meta:
        db_table = "loans"
        ordering = ["id"]
