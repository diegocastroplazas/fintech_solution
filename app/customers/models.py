from django.db import models
from django.db.models import Sum


class Customer(models.Model):
    """Customer model"""

    class Status(models.IntegerChoices):
        ACTIVE = 1, "Active"
        INACTIVE = 2, "Inactive"

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    status = models.SmallIntegerField(choices=Status.choices, default=Status.ACTIVE)
    score = models.DecimalField(max_digits=12, decimal_places=2)
    pre_approved_at = models.DateTimeField()

    @property
    def total_debt(self) -> dict:
        return self.loan_set.filter(status__in=[1, 2]).aggregate(
            Sum("outstanding_amount", default=0)
        )["outstanding_amount__sum"]

    @property
    def available_amount(self):
        return self.score - self.total_debt

    def __str__(self):
        return f"{self.id} - {self.external_id}"

    class Meta:
        db_table = "customers"
        ordering = ["id"]
