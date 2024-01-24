from django.db import models


class Customer(models.Model):
    """Customer model"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, unique=True)
    status = models.SmallIntegerField()
    score = models.DecimalField(max_digits=12, decimal_places=2)
    pre_approved_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        db_table = "customers"
        ordering = ["id"]
