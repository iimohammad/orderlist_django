from django.db import models
from userauths.models import User


class PurchaseOrder(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PurchaseOrderItem(models.Model):
    
    # Types of Membership
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.PROTECT,
        related_name='items')
    product = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return self.product