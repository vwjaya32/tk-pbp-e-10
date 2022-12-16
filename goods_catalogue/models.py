from django.db import models
from homepage.models import *
		
class CatalogueManager(models.Manager):
	def get_by_natural_key(self, name, price, imageURL):
		return self.get(name=name, price=price, imageURL=imageURL)

class Catalogue(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	image = models.ImageField(upload_to='upload/', null=True, blank=True)

	objects = CatalogueManager()

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def natural_key(self):
		return {'name': self.name, 
			'price': self.price,
			'imageURL': self.imageURL,
			}

class SoulComforter(Catalogue):
	comfortrate = models.IntegerField()
	object = CatalogueManager()

	def get_parent(self):
		return super()
	
	# def natural_key(self):
	# 	return {'name': self.name, 
	# 		'price': self.price,
	# 		'imageURL': self.imageURL,
	# 		}

class HappinessBoost(Catalogue):
	boostrate = models.IntegerField()
	object = CatalogueManager()

	def get_parent(self):
		return super()

	def natural_key(self):
		return {'name': self.name, 
			'price': self.price,
			'imageURL': self.imageURL,
			}

PILIHAN_PEMBAYARAN = (
    ('BCA', "BCA"), ('OVO', 'OVO'), ('DANA', 'DANA'), ('SHOPEEPAY', 'SHOPEEPAY'), ('GOPAY', 'GOPAY'))
PILIHAN_KURIR = (
    ('JNE', 'JNE'), ('TIKI', 'TIKI'), ('SiCepat', 'SiCepat'), ('J&T', 'J&T'))

# Create your models here.
class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, default = None, blank = True)
    nama_item = models.CharField(max_length = 255, default = "")
    metode_pembayaran = models.CharField(max_length = 255, choices = PILIHAN_PEMBAYARAN, default= PILIHAN_PEMBAYARAN[0], verbose_name= "Metode Pembayaran")
    metode_pengiriman = models.CharField(max_length = 255, choices = PILIHAN_KURIR, default=PILIHAN_KURIR[0], verbose_name= "Metode Pengiriman")

