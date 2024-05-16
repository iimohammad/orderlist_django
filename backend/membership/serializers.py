from rest_framework import serializers
from .models import Membership

class MembershipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Membership
        fields = ['id', 'membership', 'period', 'price']
        # read_only_fields = ['price']