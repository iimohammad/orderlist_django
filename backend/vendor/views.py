from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, Collection, Part, OrderResponse, Brand
from .serializers import (
    VendorSerializer,
    CollectionSerializer,
    PartSerializer,
    OrderResponseSerializer,
    BrandSerializer,
)
from .pagination import DefaultPagination

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    pagination_class = DefaultPagination
    
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = DefaultPagination
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = DefaultPagination
    
class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    pagination_class = DefaultPagination
    
class OrderResponseViewSet(ModelViewSet):
    queryset = OrderResponse.objects.all()
    serializer_class = OrderResponseSerializer
    pagination_class = DefaultPagination