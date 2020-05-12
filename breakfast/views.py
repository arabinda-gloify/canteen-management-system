from django.shortcuts import render
from rest_framework import generics
from breakfast.serializers import BreakfastSerializer
from breakfast.models import Breakfast

# Create your views here.

class BreakfastListView(generics.ListCreateAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer

class BreakfastDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Breakfast.objects.all()
	serializer_class = BreakfastSerializer