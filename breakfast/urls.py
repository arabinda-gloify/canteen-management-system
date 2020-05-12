from django.urls import path
from breakfast.views import BreakfastListView, BreakfastDetailView



urlpatterns = [
    
    path('', BreakfastListView.as_view()),
    path('<pk>/', BreakfastDetailView.as_view()),
]
