from django.shortcuts import render
from . models import Menu 
from menu.serializers import MenuSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class MenuListView(ListAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer