from django.db import models
from homepage.models import Customer
from goods_catalogue.models import Catalogue
import json

class OrderManager(models.Manager):
	def get_by_natural_key(self, customer, date_ordered, is_complete, transaction_id):
		if is_complete:
			order_status = 1
		else:
			order_status = 0
		return self.get(
			customer=customer.id,
			date_ordered=date_ordered,
			is_complete=order_status,
			transaction_id=transaction_id,
			)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	is_complete = models.BooleanField(default=False)
	on_process = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	def natural_key(self):
		if self.is_complete:
			order_status = 1
		else:
			order_status = 0
		return {
			'orderId': self.id,
			'customer': self.customer.id, 
			'date_ordered': self.date_ordered,
			'is_complete': order_status,
			'transaction_id': self.transaction_id,
			}

# class OrderItemManager(models.Manager):
# 	def get_by_natural_key(self, product, order, quantity, total_price, date_added):
# 		return self.get(
# 			product=product, 
# 			order=order, 
# 			quantity=quantity, 
# 			total_price=total_price, 
# 			date_added=date_added
# 			)

class OrderItem(models.Model):
	product = models.ForeignKey(Catalogue, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	# def natural_key(self):
	# 	return {
	# 		'product': self.product, 
	# 		'order': self.order,
	# 		'quantity': self.quantity,
	# 		'total_price': self.get_total,
	# 		'date_added': self.date_added,
	# 		}

	def get_json(self):
		json_data = {
			'product': {
				'name': self.product.name,
				'price': self.product.price,
				'image': self.product.imageURL
			},
			'quantity': self.quantity,
			'date_added': self.date_added.isoformat(),
			'order': self.order
		}
		return json.dumps(json_data)
	