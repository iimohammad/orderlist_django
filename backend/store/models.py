from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
    
# Create your models
class Vendee(models.Model):
    """Represents a vendee entity"""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'Vendee'
        verbose_name_plural = 'Vendees'
        ordering = ['user__first_name', 'user__last_name']
        
    
class Order(models.Model):
    """Represents an order entity"""
    
    # Types of status
    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED = 'F'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Complete'),
        (STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    vendee = models.ForeignKey(Vendee, on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'Order'
        verbose_name_plural = 'Orders'
        
        
class OrderItem(models.Model):
    """Represents an order item entity"""
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    quantity = models.PositiveSmallIntegerField()
    part = models.ForeignKey('vendor.Part', on_delete=models.CASCADE)
    

class SelectedVendor(models.Model):
    """Represents Selected Vendors"""
    vendee = models.OneToOneField(Vendee, on_delete=models.CASCADE)
    vendor = models.ManyToManyField('vendor.Vendor')
    
    def __str__(self):
        return self.vendee.user.username
    
    class Meta:
        db_table = 'SelectedVendor'
        verbose_name_plural = 'SelectedVendors'