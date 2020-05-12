from rest_framework import serializers
from .models import Menu
# from breakfast.serializers import BreakfastSerializer



class MenuSerializer(serializers.ModelSerializer):
	# breakfast_inside_menu = BreakfastSerializer(read_only=True, many=True)
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
			'breakfast_inside_menu',
		]

		read_only_fields = ["id", "is_active"]

