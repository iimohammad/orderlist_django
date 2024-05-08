from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import Vendee, Order, OrderItem, SelectedVendor
from .serializers import VendeeSerializer, OrderSerializer, OrderItemSerializer, SelectedVendorSerializer

# Create your views here.
class VendeeViewSet(ModelViewSet):
    queryset = Vendee.objects.all()
    serializer_class = VendeeSerializer
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def create(self, request, *args, **kwargs):
        order = Order.objects.get(pk=request.data['order'])
        part = request.data['part']
        quantity = int(request.data['quantity'])
        
        # Check if an order item with the same part already exists in the order
        existing_order_item = OrderItem.objects.filter(order=order, part=part).first()
        
        if existing_order_item:
            # If the order item already exists, update its quantity
            existing_order_item.quantity += quantity
            existing_order_item.save()
            serializer = self.get_serializer(existing_order_item)
            return Response(serializer.data)
        else:
            # If the order item does not exist, create a new one
            return super().create(request, *args, **kwargs)
    
class SelecteVendorViewSet(ModelViewSet):
    queryset = SelectedVendor.objects.all()
    serializer_class = SelectedVendorSerializer