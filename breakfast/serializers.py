from rest_framework import serializers
from breakfast.models import Breakfast
from menu.serializers import MenuSerializer



class BreakfastSerializer(serializers.ModelSerializer):
	breakfast_inside_menu = MenuSerializer(read_only=True, many=True)
	class Meta:
		model = Breakfast
		fields = [
			'id', 
			'item_name',
			'item_price',
			'breakfast_inside_menu',
		]

		read_only_fields = ["id", "is_active"]



	