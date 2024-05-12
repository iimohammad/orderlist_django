from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderItem
from store.serializers import *
from userauths.serializers import UserSerializer


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = ['id', 'order', 'product']
        read_only_fields = ['id']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.user and not request.user.is_staff:
    #         self.fields['user'].queryset = request.user.profile_set.all()


# class AdminPurchaseOrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: PurchaseOrderItem
#         fields = ['id', 'order', 'product', 'quantity']
#         read_only_fields = ['id', 'price']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    items = PurchaseOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'creator', 'created_at', 'items']
        read_only_fields = ['id', 'created_at']
