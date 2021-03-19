from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Order, Order_Item, Product
# from . serializers import OrderSerializer, OrderItemSerializer 
# from rest_framework import viewsets
# from rest_framework import permissions

import json

@login_required
def pos_order(request):
	list_of_product = Product.objects.all()

	return render(request, 'pos_order.html',{
		'products': list_of_product,
		})

def cobaorder(request):
	orders = Order.objects.filter(id=48)
	return render(request, 'receipttoprint.html',{
		'orders': orders,
		})

@login_required
def getorder(request):
	if request.method == 'POST':
		data = json.loads(request.POST.get('data', None))
		if data is None:
			raise AttributeError
		print(data)
		user = User.objects.get(username=data['username'])
		order = Order.objects.create(user_id=user.id,
												customer_name=data['customer_name'],
												total_price=data['total_price'])
		for product_id in data['product_ids']:
			Order_Item(product=Product.objects.get(pk=product_id[0]), order=order, quantity=product_id[1]).save()
		# if data['total_price'] <= customer.balance:
		# 	customer.balance -= int(data['total_price'])
		# 	customer.save()
			# order.success = True
		order.save()
		# return render(request, 'order.html', {'success' : order.success})
		orders = Order.objects.filter(id=order.id)
		return render(request, 'receipttoprint.html',{
			'orders': orders,
		})

# class OrderViewSet(viewsets.ModelViewSet):
# 	"""
# 	API endpoint that allows users to be viewed or edited.
# 	"""
# 	# queryset = Order.objects.all().order_by('-last_change_timestamp')
# 	queryset = Order.objects.all()
# 	serializer_class = OrderSerializer
# 	permission_classes = [permissions.IsAuthenticated]

# class OrderItemViewSet(viewsets.ModelViewSet):
# 	"""
# 	API endpoint that allows users to be viewed or edited.
# 	"""
# 	# queryset = Order.objects.all().order_by('-last_change_timestamp')
# 	queryset = Order_Item.objects.all()
# 	serializer_class = OrderItemSerializer
# 	permission_classes = [permissions.IsAuthenticated]