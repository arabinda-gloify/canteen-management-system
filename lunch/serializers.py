from rest_framework import serializers
from lunch.models import Lunch 

class LunchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lunch
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]