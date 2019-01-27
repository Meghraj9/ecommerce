from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField( max_length=20)
	discription = models.TextField()
	price 		= models.DecimalField(max_digits =20, decimal_places=2, default=39.99)

	def __str__(self):
		return self.title 