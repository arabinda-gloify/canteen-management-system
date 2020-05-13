from django.shortcuts import render
from rest_framework import generics
from dinner.models import Dinner
from dinner.serializers import DinnerSerializer
from rest_framework.permissions import (
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 
# Create your views here.

class DinnerListCreateView(generics.ListCreateAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]

	search_fields = [
				'item_name', 
				'item_price',
			]

class DinnerDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	
	search_fields = [
				'item_name', 
				'item_price',
			]