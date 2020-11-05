from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('api/get_lecturer/', views.get_lecturer),
	path('api/get_struct/', views.set_struct),
	path('api/get_programmes/', views.get_programmes)
]
