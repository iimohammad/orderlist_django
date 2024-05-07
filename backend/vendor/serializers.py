from .models import Vendor, Collection, Part
from rest_framework import serializers

        
class VendorSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Vendor
        fields = ['user', 'user_username']
        
        
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name', 'description', 'vendor']
        
        
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['name', 'part_number', 'description', 'part_brochure', 'collection', 'vendor']