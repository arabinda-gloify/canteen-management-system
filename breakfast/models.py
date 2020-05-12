from django.db import models
from user.models import User
from menu.models import Menu


# Create your models here.

	
class Breakfast(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name="breakfast_under_menu")
	item_name = models.CharField(default="", blank=True, max_length=250)
	item_price = models.DecimalField(max_digits=6, decimal_places=2, default="")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")

	def __str__(self):
		return self.item_name

