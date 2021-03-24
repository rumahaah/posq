from django.db import models
from django.conf import settings
from django.utils import timezone
# from sequences import get_next_value
# from sequences.models import Sequence


# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	stock_applies = models.BooleanField()
	minimum_stock = models.PositiveSmallIntegerField(default=0)
	stock = models.IntegerField(default=0)
	code = models.CharField(max_length=50, unique=True, null=True, blank=True)
	#
	last_change_timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	creation_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "%s(%s) " % (self.name, self.price)

class Sequence(models.Model):
	name = models.CharField(max_length=100, primary_key=True)
	number = models.PositiveIntegerField()

	def __str__(self):
		return "%s - " % (self.name)

class Order(models.Model):
	uniqnumber = "JD-00000000"
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=100)
	order_number = models.CharField(max_length=12, default=uniqnumber, blank=True)
	total_price = models.DecimalField(max_digits=10,
									  decimal_places=2,
									  default=0)
	#
	last_change_timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	# creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)
	creation_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	def __str__(self):
		return "%s(%s) " % (self.customer_name, self.total_price)


class Cash(models.Model):
	amount = models.DecimalField(max_digits=12,
								 decimal_places=2,
								 default=0)
	#
	last_change_timestamp = models.DateField(auto_now=True, auto_now_add=False)
	creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)

class OrderItem(models.Model):
	product = models.ForeignKey(Product,
								on_delete=models.CASCADE)
	quantity = models.IntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	#
	last_change_timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	# creation_timestamp = models.DateField(auto_now=False, auto_now_add=True)
	creation_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return "%s | %s - Qty (%s) " % (self.order, self.product, self.quantity)