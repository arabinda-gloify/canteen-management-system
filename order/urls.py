from django.urls import path
from order import views

urlpatterns = [
	path('', views.OrderAPI.as_view()),
	path('items/', views.ItemAPI.as_view()),
]