from django.contrib import admin
from .models import Vendor, Collection, Part, PartImage, Brand

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Collection)
admin.site.register(Part)
admin.site.register(PartImage)
admin.site.register(Brand)