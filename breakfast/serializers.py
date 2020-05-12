from rest_framework import serializers
from breakfast.models import Breakfast



class BreakfastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Breakfast
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]



	