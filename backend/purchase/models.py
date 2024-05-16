from django.db import models
from store.models import Product
from user_panel.models import CustomUser
from uuid import uuid4


class wallet(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def add_to_balance(self, amount):
        self.balance += amount
        self.save()

    def deduct_from_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=False)
    # profile = models.OneToOneField(wallet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    def add_to_cart(self, product_id, quantity=1):
        product = Product.objects.get(pk=product_id)
        if product:
            cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return True
        return False

    def remove_from_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = [['cart', 'product']]

    def update_quantity(self, quantity):
        self.quantity = quantity
        self.save()

    def __str__(self):
        return f"CartItem {self.id}"
