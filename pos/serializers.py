from rest_framework import serializers
from . models import Order, Order_Item


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'total_price', 'last_change_timestamp')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = ('id', 'product', 'order', 'last_change_timestamp')
