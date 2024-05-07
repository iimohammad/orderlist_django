from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, Collection, Part
from .serializers import VendorSerializer, CollectionSerializer, PartSerializer

# Create your views here.
class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer