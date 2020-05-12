from rest_framework import serializers
from .models import Menu
from breakfast.serializers import BreakfastSerializer
from today_special.serializers import TodaySpecialSerializer
from lunch.serializers import LunchSerializer
from snacks.serializers import SnacksSerializer



class MenuSerializer(serializers.ModelSerializer):
	breakfast = BreakfastSerializer(read_only=True, many=True)
	today_special = TodaySpecialSerializer(read_only=True, many=True)
	lunch = LunchSerializer(read_only=True, many=True)
	snacks = SnacksSerializer(read_only=True, many=True)
	class Meta:
		model = Menu
		fields = [
			'id', 
			'name',
			'description',
			'breakfast',
			'today_special',
			'lunch',
			'snacks',
		]

		read_only_fields = ["id", "is_active"]

