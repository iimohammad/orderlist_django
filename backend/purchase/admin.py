from django.contrib import admin
from .models import wallet, Cart, CartItem


class CartItemInline(admin.StackedInline):
    extra = 0
    model = CartItem


@admin.register(wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'balance', 'created_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']
