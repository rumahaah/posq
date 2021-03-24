from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from . models import Order, OrderItem, Product, Sequence
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

@login_required
def cobaorder(request):
	orders = Order.objects.filter(id=48)
	return render(request, 'receipttoprint.html',{
		'orders': orders,
		})

def ordernumber():
	if len(str(timezone.localtime().month)) == 1 :
		month = '0' + str(timezone.localtime().month)
	else:
		month = str(timezone.localtime().month)
	name_sequence = str(timezone.localtime().day)+str(timezone.localtime().month)+str(timezone.localtime().year)
	
	try:
		number_sequence = Sequence.objects.get(name=name_sequence).number
	except ObjectDoesNotExist:
		Sequence(name=name_sequence, number=1).save()
		number_sequence = Sequence.objects.get(name=name_sequence).number

	if len(str(number_sequence)) == 1:
		number_sequence_str = '00' + str(number_sequence)
	elif len(str(number_sequence)) == 2:
		number_sequence_str = '0' + str(number_sequence)
	else:
		number_sequence_str = str(number_sequence)

	uniqnumber = "JD-%s%s-%s" % (month, timezone.localtime().day, number_sequence_str)
	
	return [name_sequence, uniqnumber, number_sequence]

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
												total_price=data['total_price'],
												order_number=ordernumber()[1])
		for product_id in data['product_ids']:
			OrderItem(product=Product.objects.get(pk=product_id[0]), order=order, quantity=product_id[1]).save()
		# if data['total_price'] <= customer.balance:
		# 	customer.balance -= int(data['total_price'])
		# 	customer.save()
			# order.success = True
		order.save()

		# add Sequence
		Sequence.objects.filter(name=ordernumber()[0]).update(number=(ordernumber()[2]+1))

		orders = Order.objects.filter(id=order.id)
		return render(request, 'receipttoprint.html',{
			'orders': orders,
		})

def reportorder(request):
	orders = Order.objects.all()
	return render(request, 'reportorder.html',{
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