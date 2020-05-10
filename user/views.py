from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
									IsAuthenticated,
									AllowAny,
									IsAdminUser,
									) 

# Create your views here.

class UserModelViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [AllowAny,]
	

	search_fields = ('first_name',)
	ordering_fields = ('id',)