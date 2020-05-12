from rest_framework import serializers
from .models import Menu
from breakfast.serializers import BreakfastSerializer


class MenuSerializer(serializers.ModelSerializer):
	breakfast = BreakfastSerializer(read_only=True, many=True)
	class Meta:
		model = Menu
		fields = [
			'id', 
			'name',
			'description',
			'breakfast',
		]

		read_only_fields = ["id", "is_active"]

