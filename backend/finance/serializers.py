from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem
from store.serializers import *
from user_panel.serializers import CustomUserSerializer


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'order', 'product', 'quantity']
        read_only_fields = ['id', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user and not request.user.is_staff:
            self.fields['user'].queryset = request.user.profile_set.all()


class AdminPurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model: PurchaseOrderItem
        fields = ['id', 'order', 'product', 'quantity']
        read_only_fields = ['id', 'price']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer(read_only=True)
    items = PurchaseOrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'creator', 'created_at', 'items', 'total_price']
        read_only_fields = ['id', 'created_at', 'total_price']

    def get_total_price(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.quantity * item.product.price
        return total
