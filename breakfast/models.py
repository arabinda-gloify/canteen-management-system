from django.db import models
from user.models import User


# Create your models here.

	
class Breakfast(models.Model):
	item_name = models.CharField(default="", blank=True, max_length=250)
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='breakfast_created_by')
	updated_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='breakfast_updated_by')

	def __str__(self):
		return self.item_name

