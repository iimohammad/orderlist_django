from django.contrib import admin
from .models import Vendee, Order, OrderItem, SelectedVendor

# Register your models here.
admin.site.register(Vendee)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SelectedVendor)