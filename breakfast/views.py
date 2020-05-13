from django.shortcuts import render
from rest_framework import generics
from breakfast.serializers import BreakfastSerializer
from breakfast.models import Breakfast
from rest_framework.permissions import (
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 

# Create your views here.

class BreakfastListView(generics.ListCreateAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]

class BreakfastDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer
	permission_classes = [IsAdminUser,]

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]