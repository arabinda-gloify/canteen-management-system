from django.urls import path
from menu.views import MenuListView

urlpatterns = [
	path('', MenuListView.as_view()),
]