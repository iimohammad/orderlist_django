from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from store.models import Order, Vendee


# Create your models
class Brand(models.Model):
    """Represents a brand entity"""
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Brand'
        verbose_name_plural = 'Brands'
    
       
class Vendor(models.Model):
    """Represents a vendor entity"""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['user__first_name', 'user__last_name']
        
        
        
class Collection(models.Model):
    """Represents a collection entity"""
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    vendor = models.ManyToManyField(
        Vendor,
        verbose_name='Vendors',
        blank=True)
    brand = models.ManyToManyField(Brand)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Collection'
        verbose_name_plural = 'Collections'
        
        

class Part(models.Model):
    """Represents a part entity"""
    
    name = models.CharField(max_length=255)
    part_number = models.TextField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    price = MoneyField(
        max_digits=14,
        decimal_places=0,
        default_currency='IRR',
        blank=True,
        null=True)
    description = models.TextField()
    part_brochure = models.FileField(
        upload_to='vendors/brochures',
        blank=True,
        null=True)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT)
    vendor = models.ManyToManyField(Vendor, verbose_name='Vendors')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Part'
        verbose_name_plural = 'Parts'
        
        
class PartImage(models.Model):
    """Represents a part Image entity"""
    part = models.ForeignKey(
        Part, on_delete=models.CASCADE, related_name='images')
    part_image = models.ImageField(
        upload_to='vendors/images',
        blank=True,
        null=True)
    
    class Meta:
        db_table = 'PartImage'
        verbose_name_plural = 'images'
        
        
class OrderResponse(models.Model):
    """Represents an order response entity"""
    
    # Types of Response
    RESPONSE_AVAILABLE = 'A'
    RESPONSE_NOT_AVAILABLE = 'NA'
    RESPONSE_NOT_RELATED = 'NR'
    RESPONSE_PENDING = 'P'
    RESPONSE_CHOICES = [
        (RESPONSE_AVAILABLE, 'Available'),
        (RESPONSE_NOT_AVAILABLE, 'Not Available'),
        (RESPONSE_NOT_RELATED, 'Not Related'),
        (RESPONSE_PENDING, 'Pending')
    ]
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    response = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=RESPONSE_PENDING)
    delivery_date = models.DateField()
    description = models.TextField()
    
    
    class Meta:
        db_table = 'OrderResponse'
        verbose_name_plural = 'OrderResponses'