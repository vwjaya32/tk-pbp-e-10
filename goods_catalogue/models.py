from django.db import models
		
class CatalogueManager(models.Manager):
	def get_by_natural_key(self, item_name, item_price, imageURL):
		return self.get(name=item_name, price=item_price, imageURL=imageURL)

class Catalogue(models.Model):
	item_name = models.CharField(max_length=255)
	item_price = models.FloatField()
	item_picture = models.ImageField(upload_to='upload/', null=True, blank=True)

	objects = CatalogueManager()

	def __str__(self):
		return self.item_name

	@property
	def imageURL(self):
		try:
			url = self.item_picture.url
		except:
			url = ''
		return url

	def natural_key(self):
		return {'name': self.item_name, 
			'price': self.item_price,
			'imageURL': self.imageURL,
			}

class SoulComforter(Catalogue):
	max_comfort = models.IntegerField()
	object = CatalogueManager()

	def get_parent(self):
		return super()
	
	# def natural_key(self):
	# 	return {'name': self.name, 
	# 		'price': self.price,
	# 		'imageURL': self.imageURL,
	# 		}

class AnxietyBoost(Catalogue):
	boostrate = models.IntegerField()
	object = CatalogueManager()

	def get_parent(self):
		return super()

	def natural_key(self):
		return {'name': self.item_name, 
			'price': self.item_price,
			'imageURL': self.imageURL,
			}

