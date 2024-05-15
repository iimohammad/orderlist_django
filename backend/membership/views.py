from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Membership
from .serializers import MembershipSerializer

# Create your views here.
class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer