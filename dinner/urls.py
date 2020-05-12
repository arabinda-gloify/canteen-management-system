from django.urls import path
from dinner import views

urlpatterns = [
		path('', views.DinnerListCreateView.as_view()),
		path('<pk>/', views.DinnerDetailView.as_view()),
]