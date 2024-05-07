from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendee, Order, OrderItem
from .serializers import VendeeSerializer, OrderSerializer, OrderItemSerializer

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