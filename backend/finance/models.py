from django.db import models
from userauths.models import User
from membership.models import Membership


class PurchaseOrder(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PurchaseOrderItem(models.Model):
    
    order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.PROTECT,
        related_name='items')
    product = models.ForeignKey(Membership, on_delete=models.PROTECT)

    def __str__(self):
        return self.product