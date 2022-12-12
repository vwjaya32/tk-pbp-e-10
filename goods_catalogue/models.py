from django.db import models
		
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

