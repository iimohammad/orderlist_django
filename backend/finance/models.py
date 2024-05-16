from django.db import models
<<<<<<< HEAD
from store.models import Product
from user_panel.models import CustomUser
=======
from userauths.models import User
from membership.models import Membership
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff


class PurchaseOrder(models.Model):
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.quantity * item.price
        return total


class PurchaseOrderItem(models.Model):
<<<<<<< HEAD
=======
    
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff
    order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.PROTECT,
        related_name='items')
<<<<<<< HEAD
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='purchase_order_items')
    quantity = models.PositiveSmallIntegerField(default=0)
=======
    product = models.ForeignKey(Membership, on_delete=models.PROTECT)
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff

    def __str__(self):
        return self.product
