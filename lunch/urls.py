from django.urls import path
from lunch import views

urlpatterns = [
		path('', views.LunchListCreateView.as_view()),
		path('<pk>/', views.LunchDetailView.as_view()),
]