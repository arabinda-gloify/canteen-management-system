from django.db import models
# from menu.models import Menu
from django.conf import settings
from datetime import datetime

# Create your models here.
CATEGORY_CHOICES = (
		('TS','Today Special'),
		('B','Breakfast'),
		('L','Lunch'),
		('S','Snacks'),
		('D','Dinner'),
	)
class Item(models.Model):
	title = models.CharField(max_length=50)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	category = models.CharField(
		choices=CATEGORY_CHOICES, default="", max_length=2)
	description = models.TextField(blank=True, null=True)
	quantity = models.IntegerField(default=1)
	slug = models.SlugField()


	def __str__(self):
		return f'{self.title}'

class OrderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.item}'

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, 
								on_delete=models.CASCADE)
	
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user






# class OrderItem(models.Model):
# 	ITEM_CHOICES = (
#         ("today_special", "Today_special"),
#         ("breakfast", "Breakfast"),
#         ("lunch", "Lunch"),
#         ("snacks", "Snacks"),
#         ("dinner", "Dinner"),
#     )
# 	# menu = models.ForeignKey(Menu, on_delete=models.CASCADE, help_text="Breakfast, Lunch, etc")
# 	# item_name = models.ManyToManyField(Menu, related_name="+")
# 	item_name = models.CharField(max_length=13, choices=ITEM_CHOICES, blank=True, null=True)
# 	price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

# 	def __str__(self):
# 		return f'{self.item_name}'


# class Order(models.Model):
# 	title = models.CharField(blank=True, null=True, max_length=50)
# 	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

# 	food_type = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
# 	item = models.ManyToManyField(OrderItem, on_delete=models.CASCADE)
# 	price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

# 	timestamp = models.DateTimeField(auto_now_add=True)
# 	active = models.BooleanField(default=True)

# 	class Meta:
# 		ordering = ['-timestamp', ]


