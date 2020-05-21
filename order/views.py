from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderSerializer, ItemSerializer
from .models import Order, Item

# Create your views here.

class OrderAPI(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class ItemAPI(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


