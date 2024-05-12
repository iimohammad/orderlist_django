from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import PurchaseOrder, PurchaseOrderItem
from .serializers import PurchaseOrderItemSerializer, PurchaseOrderSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return PurchaseOrder.objects.all()
        return PurchaseOrder.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return PurchaseOrderItem.objects.all()
        return PurchaseOrderItem.objects.filter(
            order__creator=self.request.user)