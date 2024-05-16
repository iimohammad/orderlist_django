from rest_framework import serializers
from userauths.models import User
from .models import Cart, CartItem
from userauths.serializers import UserSerializer


class CartItemSerializer(serializers.ModelSerializer):
    
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart']


class CartSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum(item.product.price * item.quantity for item in cart.items.all())

    class Meta:
        model = Cart
        fields = ['id', 'items', 'owner', 'total_price']

    def create(self, validated_data):
        request = self.context.get('request')
        owner = request.user
        cart = Cart.objects.create(owner=owner, **validated_data)
        return cart