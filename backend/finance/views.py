from rest_framework import viewsets, permissions
from .models import PurchaseOrder, PurchaseOrderItem
<<<<<<< HEAD
from finance.serializers import PurchaseOrderItemSerializer, PurchaseOrderSerializer
=======
from .serializers import PurchaseOrderItemSerializer, PurchaseOrderSerializer
from .pagination import DefaultPagination
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff

    def get_queryset(self):
        if self.request.user.is_staff:
            return PurchaseOrder.objects.all()
        return PurchaseOrder.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseOrderItemSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
>>>>>>> 82e75e4aff4000f74697895d98ab75f81235acff

    def get_queryset(self):
        if self.request.user.is_staff:
            return PurchaseOrderItem.objects.all()
        return PurchaseOrderItem.objects.filter(
            order__creator=self.request.user)
