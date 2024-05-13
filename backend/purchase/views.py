from django.shortcuts import render
from rest_framework import viewsets, permissions
from finance.models import PurchaseOrder, PurchaseOrderItem
from purchase.serializers import *
from .models import *
from django.db import transaction
from django.db.models import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from user_panel.models import Profile
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Cart.objects.all()
        return Cart.objects.filter(owner=self.request.user)
    

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()

        if cart.items.count() == 0:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                profile = wallet.objects.get(user=request.user)
                if profile.balance >= cart.total_price():
                    order = PurchaseOrder.objects.create(user=request.user)
                    for item in cart.items.all():
                        PurchaseOrderItem.objects.create(
                            order=order,
                            product=item.product,
                            price=item.product.price,
                            quantity=item.quantity
                        )

                    profile.balance -= cart.total_price()
                    profile.save()

                    cart.delete()

                    return Response({"message": "Checkout successful"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Insufficient balance"}, status=status.HTTP_402_PAYMENT_REQUIRED)
        except ObjectDoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
