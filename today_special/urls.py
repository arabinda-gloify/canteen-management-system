from django.urls import path
from today_special import views

urlpatterns = [
		path('', views.TodaySpecialListCreateView.as_view()),
		path('<pk>/', views.TodaySpecialDetailView.as_view()),
]