from django.shortcuts import render
from rest_framework import generics
from lunch.models import Lunch
from lunch.serializers import LunchSerializer

# Create your views here.

class LunchListCreateView(generics.ListCreateAPIView):
	queryset = Lunch.objects.all()
	serializer_class = LunchSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]

class LunchDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lunch.objects.all()
	serializer_class = LunchSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]