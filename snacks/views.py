from django.shortcuts import render
from rest_framework import generics
from snacks.models import Snacks
from snacks.serializers import SnacksSerializer
from rest_framework.permissions import (
		IsAuthenticated,
		AllowAny,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 

# Create your views here.

class SnacksListCreateView(generics.ListCreateAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class SnacksDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]