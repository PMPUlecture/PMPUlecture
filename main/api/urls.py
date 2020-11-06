from django.urls import path
from . import views

urlpatterns = [
	path('lecturers/', views.get_lecturer),
	path('struct/', views.set_struct),
	path('programmes/', views.get_programmes)
]
