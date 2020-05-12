from django.shortcuts import render
from . models import Menu 
from menu.serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
									IsAuthenticated,
									AllowAny,
									IsAdminUser,
									) 

# Create your views here.

class MenuListCreateView(ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	search_fields = (
			'name',
			'description',

		)
	ordering_fields = ('id',)
	
	# filterset_fields = []

class MenuRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	search_fields = (
			'name',
			'description',

		)
	ordering_fields = ('id',)
