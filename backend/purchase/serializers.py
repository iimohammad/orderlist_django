from rest_framework import serializers
from store.models import Product
from userauths.models import CustomUser
from .models import wallet, Cart, CartItem
from userauths.serializers import CustomUserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = wallet
        fields = ['id', 'user', 'balance', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum(item.product.price * item.quantity for item in cart.items.all())

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price', 'owner']

    def create(self, validated_data):
        request = self.context.get('request')
        owner = request.user
        cart = Cart.objects.create(owner=owner, **validated_data)
        return cart
