from django.db import models
from userauths.models import User
from uuid import uuid4
from membership.models import Membership


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_to_cart(self, product_id, quantity=1):
        product = Membership.objects.get(pk=product_id)
        if product:
            cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return True
        return False

    def remove_from_cart(self, product_id):
        product = Membership.objects.get(pk=product_id)
        if product:
            cart_item = CartItem.objects.filter(cart=self, product=product).first()
            if cart_item:
                cart_item.delete()
                return True
        return False

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Membership, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"CartItem {self.id}"