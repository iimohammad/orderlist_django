from django.contrib import admin
from .models import Wallet, Cart, CartItem

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Cart)
admin.site.register(CartItem)