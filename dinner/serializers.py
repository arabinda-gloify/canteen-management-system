from rest_framework import serializers
from dinner.models import Dinner 

class DinnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dinner
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]