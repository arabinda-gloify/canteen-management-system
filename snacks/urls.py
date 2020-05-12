from django.urls import path
from snacks import views

urlpatterns = [
		path('', views.SnacksListCreateView.as_view()),
		path('<pk>/', views.SnacksDetailView.as_view()),
]