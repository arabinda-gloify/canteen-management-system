from django.shortcuts import render
from . models import Menu 
from menu.serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
		IsAuthenticated,
		AllowAny,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 
# Create your views here.

class MenuListCreateView(ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'name', 
				'description',
			]

class MenuDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'name', 
				'description',
			]