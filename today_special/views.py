from django.shortcuts import render
from rest_framework import generics
from today_special.models import TodaySpecial
from today_special.serializers import TodaySpecialSerializer
from rest_framework.permissions import (
		IsAuthenticated,
		AllowAny,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	) 
# Create your views here.

class TodaySpecialListCreateView(generics.ListCreateAPIView):
	queryset = TodaySpecial.objects.all()
	serializer_class = TodaySpecialSerializer
	permission_classes = [IsAuthenticatedOrReadOnly,]


	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]

class TodaySpecialDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = TodaySpecial.objects.all()
	serializer_class = TodaySpecialSerializer
	permission_classes = [IsAdminUser,]


	ordering_fields = ['id',]
	search_fields = [
				'item_name', 
				'item_price',
			]