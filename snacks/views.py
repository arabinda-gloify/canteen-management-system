from django.shortcuts import render
from rest_framework import generics
from snacks.models import Snacks
from snacks.serializers import SnacksSerializer

# Create your views here.

class SnacksListCreateView(generics.ListCreateAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]

class SnacksDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snacks.objects.all()
	serializer_class = SnacksSerializer

	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]