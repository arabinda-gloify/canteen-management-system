from django.db import models
from menu.models import Menu

# Create your models here.


class OrderItem(models.Model):
	ITEM_CHOICES = (
        ("today_special", "Today_special"),
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("snacks", "Snacks"),
        ("dinner", "Dinner"),
    )
	# menu = models.ForeignKey(Menu, on_delete=models.CASCADE, help_text="Breakfast, Lunch, etc")
	# item_name = models.ManyToManyField(Menu, related_name="+")
	item_name = models.CharField(max_length=13, choices=ITEM_CHOICES, blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

	def __str__(self):
		return f'{self.item_name}'


class Order(models.Model):
	title = models.CharField(blank=True, null=True, max_length=50)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

	food_type = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
	item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
	price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-timestamp', ]


