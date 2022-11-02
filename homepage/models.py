from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length=255, null=True)
	is_technician = models.BooleanField(default=False)
	phone = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.name

class AddressManager(models.Manager):
	def get_by_natural_key(self, id, customer, address, kota, kecamatan, kelurahan, postcode):
		return self.get(
			id=id,
			customer=customer,
			address=address,
			kota=kota,
			kecamatan=kecamatan,
			kelurahan=kelurahan,
			postcode=postcode,
			)

class Address(models.Model):
	id = models.BigAutoField(primary_key=True)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	kota = models.CharField(max_length=200, null=False)
	kecamatan = models.CharField(max_length=200, null=False)
	kelurahan = models.CharField(max_length=200, null=False)
	postcode = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.address
	
	def natural_key(self):
		return {
			'id': self.id,
			'customer': self.customer,
			'address': self.address, 
			'kota': self.kota,
			'kecamatan': self.kecamatan,
			'kelurahan': self.kelurahan,
			'postcode': self.postcode,
			}
