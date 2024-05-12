from django.db import models
# from store.models import Product
# from userauths.models import User


# class PurchaseOrder(models.Model):
#     creator = models.ForeignKey(
#         CustomUser,
#         on_delete=models.PROTECT,
#         editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.id)

#     def total_price(self):
#         total = 0
#         for item in self.items.all():
#             total += item.quantity * item.price
#         return total


# class PurchaseOrderItem(models.Model):
#     order = models.ForeignKey(
#         PurchaseOrder,
#         on_delete=models.PROTECT,
#         related_name='items')
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.PROTECT,
#         related_name='purchase_order_items')
#     quantity = models.PositiveSmallIntegerField(default=0)

#     def __str__(self):
#         return self.product