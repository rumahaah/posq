from django.contrib import admin
from . models import Product, Order, Cash, Order_Item

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cash)
admin.site.register(Order_Item)