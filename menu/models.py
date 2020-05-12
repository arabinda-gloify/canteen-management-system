from django.db import models
from user.models import User


# Create your models here.

class Menu(models.Model):
	name = models.CharField(default="Today's Menu", blank=True, null=True, max_length=255)
	description = models.TextField(blank=True, null=True)
	is_active = models.BooleanField(default=True)	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='+')
	updated_by = models.ForeignKey(User, 
									on_delete=models.CASCADE, null=True,
									related_name='+')
	
	def __str__(self):
		return self.name

