from .models import Vendee, Order, OrderItem
from rest_framework import serializers

class VendeeSerializer(serializers.ModelSerializer):
        user_username = serializers.CharField(source='user.username', read_only=True)
        
        class Meta:
            model = Vendee
            fields = ['user', 'user_username']
            
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'part']
            
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