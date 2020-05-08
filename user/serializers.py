from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
	is_active = serializers.ReadOnlyField()
	email = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	class Meta:
		model = User
		fields = [
			"id",
			"email",
			"contact_no",
			"first_name",
			"last_name",
			"gender",
			"is_active",
			"created_at",
		]
