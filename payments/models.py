from django.db import models


class Payment(models.Model):
    """Payment model"""

    class Status(models.IntegerChoices):
        PENDING = 1, "Pending"
        PAID = 2, "Paid"
        REJECTED = 3, "Rejected"

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.SmallIntegerField(choices=Status.choices, default=Status.PENDING)
    paid_at = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)

    def __str__(self):
        return f"Payment: {self.id} - {self.external_id}"

    class Meta:
        db_table = "payments"
        ordering = ["id"]


class PaymentDetail(models.Model):
    """PaymentDetail model"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment = models.ForeignKey("payments.Payment", on_delete=models.CASCADE)
    loan = models.ForeignKey("loans.Loan", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    fee = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"PaymentDetail: {self.id} - {self.payment.external_id}"

    class Meta:
        db_table = "payment_details"
        ordering = ["id"]
