from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from finance.models import PurchaseOrder, PurchaseOrderItem
from purchase.serializers import *
from .models import *
from django.db import transaction
from django.db.models import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from .pagination import DefaultPagination
from userauths.models import Profile
from rest_framework.permissions import IsAuthenticated


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(owner=self.request.user)
    

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()

        if cart.items.count() == 0:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
        


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination