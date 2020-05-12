from django.urls import path
from menu.views import MenuListCreateView, MenuDetailView

urlpatterns = [
	path('', MenuListCreateView.as_view()),
	path('<pk>/', MenuDetailView.as_view()),
]