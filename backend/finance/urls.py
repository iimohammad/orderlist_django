from rest_framework.routers import DefaultRouter
from django.urls import path, include
from finance.views import PurchaseOrderItemViewSet, PurchaseOrderViewSet

router = DefaultRouter()

router.register(
    'PurchaseOrder',
    PurchaseOrderViewSet,
    basename='PurchaseOrder')
router.register(
    'PurchaseOrderItem',
    PurchaseOrderItemViewSet,
    basename='PurchaseOrderItem')

urlpatterns = [
    path('', include(router.urls)),
]
