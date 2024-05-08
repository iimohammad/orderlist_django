from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, Collection, Part, OrderResponse, Brand
from .serializers import VendorSerializer, CollectionSerializer, PartSerializer, OrderResponseSerializer, BrandSerializer

# Create your views here.
class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    
class OrderResponseViewSet(ModelViewSet):
    queryset = OrderResponse.objects.all()
    serializer_class = OrderResponseSerializer