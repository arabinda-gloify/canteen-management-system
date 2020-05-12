from rest_framework import serializers
from snacks.models import Snacks 

class SnacksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snacks
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]