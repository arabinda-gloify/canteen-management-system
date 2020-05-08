from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

class UserModelViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated,]


	search_fields = ('first_name',)
	ordering_fields = ('id',)