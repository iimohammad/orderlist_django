from django.contrib import admin
from .models import Vendee, Order, OrderItem

# Register your models here.
admin.site.register(Vendee)
admin.site.register(Order)
admin.site.register(OrderItem)