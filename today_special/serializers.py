from rest_framework import serializers
from today_special.models import TodaySpecial


class TodaySpecialSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodaySpecial
		fields = [
			'id', 
			'item_name',
			'item_price',
		]

		read_only_fields = ["id", "is_active"]