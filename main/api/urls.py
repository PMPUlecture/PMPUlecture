from django.urls import path
from . import views

urlpatterns = [
	path(r"lecturer/<int:id>", views.get_lecturer),
	path('struct/', views.set_struct),
	path('programmes/', views.get_programmes)
]
