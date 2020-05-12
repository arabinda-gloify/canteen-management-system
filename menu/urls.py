from django.urls import path
from menu.views import MenuListCreateView, MenuRetrieveUpdateDestroyView

urlpatterns = [
	path('', MenuListCreateView.as_view()),
	path('<pk>/', MenuRetrieveUpdateDestroyView.as_view()),
]