from django.shortcuts import render
from . models import Menu 
from menu.serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class MenuListCreateView(ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	ordering_fields = ['id',]
	search_fields = [
				'name', 
				'description',
			]

class MenuDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	ordering_fields = ['id',]
	search_fields = [
				'name', 
				'description',
			]