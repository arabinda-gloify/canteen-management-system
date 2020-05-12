from django.shortcuts import render
from rest_framework import generics
from dinner.models import Dinner
from dinner.serializers import DinnerSerializer

# Create your views here.

class DinnerListCreateView(generics.ListCreateAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]

class DinnerDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Dinner.objects.all()
	serializer_class = DinnerSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]