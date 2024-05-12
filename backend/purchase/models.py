from django.db import models
from userauths.models import User
from uuid import uuid4


class wallet(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def add_to_cart(self, product_id, quantity=1):
    #     product = Product.objects.get(pk=product_id)
    #     if product:
    #         cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
    #         if not created:
    #             cart_item.quantity += quantity
    #             cart_item.save()
    #         return True
    #     return False

    # def remove_from_cart(self, product_id):
    #     product = Product.objects.get(pk=product_id)
    #     if product:
    #         cart_item = CartItem.objects.filter(cart=self, product=product).first()
    #         if cart_item:
    #             cart_item.delete()
    #             return True
    #     return False

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    
    # Types of Membership
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE)


    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"CartItem {self.id}"