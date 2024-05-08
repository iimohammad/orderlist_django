from .models import Vendee, Order, OrderItem, SelectedVendor
from rest_framework import serializers

class VendeeSerializer(serializers.ModelSerializer):
        user_username = serializers.CharField(source='user.username', read_only=True)
        
        class Meta:
            model = Vendee
            fields = ['user', 'user_username']
            
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'part', 'order']
        
    # def create(self, validated_data):
    #     order = validated_data['order']
    #     part = validated_data['part']
    #     quantity = validated_data['quantity']
        
    #     # Check if an order item with the same part already exists in the order
    #     existing_order_item = OrderItem.objects.filter(order=order, part=part).first()
        
    #     if existing_order_item:
    #         # If the order item already exists, update its quantity
    #         existing_order_item.quantity += quantity
    #         existing_order_item.save()
    #         return existing_order_item
    #     else:
    #         # If the order item does not exist, create a new one
    #         return super().create(validated_data)
            
class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True)
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='orderitem-detail'
    )
    
    class Meta:
        model = Order
        fields = ['id', 'vendee', 'placed_at', 'status', 'items']
        
        
class SelectedVendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SelectedVendor
        fields = ['id', 'vendee', 'vendor']