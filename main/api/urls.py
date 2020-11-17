from django.urls import path
from . import views

urlpatterns = [
	path("lecturer/<int:id>", views.DetailLecturer.as_view()),
	path("lecturer/", views.DetailLecturer.as_view()),
	path("material/", views.DetailMaterial.as_view()),
	path("subjects/", views.SubjectsView.as_view()),
	path("programmes/", views.Programmes.as_view()),
	path("user/", views.UserDetail.as_view())
]
