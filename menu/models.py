from django.db import models
from user.models import User
from today_special.models import TodaySpecial
from breakfast.models import Breakfast
from lunch.models import Lunch
from snacks.models import Snacks
from dinner.models import Dinner



# Create your models here.

class Menu(models.Model):
	name = models.CharField(default="Today's Menu", blank=True, null=True, max_length=255)
	description = models.TextField(blank=True, null=True)
	today_special = models.ForeignKey(TodaySpecial, on_delete=models.CASCADE, null=True)
	breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, null=True)
	lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, null=True)
	snacks = models.ForeignKey(Snacks, on_delete=models.CASCADE, null=True)
	dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, null=True)
	is_active = models.BooleanField(default=True)	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='menu_created_by')
	updated_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='menu_updated_by')
	
	def __str__(self):
		return self.name

