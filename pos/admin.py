from django.contrib import admin
from . models import Product, Order, Cash, OrderItem, Sequence

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cash)
admin.site.register(OrderItem)
admin.site.register(Sequence)