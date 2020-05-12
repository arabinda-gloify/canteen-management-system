from rest_framework import serializers
from .models import Menu



class MenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = [
			'id', 
			'name',
			'description',
			'today_special',
			'breakfast',
			'lunch',
			'snacks',
			'dinner',
			'is_active',
		]

		read_only_fields = ["id", "is_active"]

