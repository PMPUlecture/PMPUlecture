from django.urls import path
from . import views

urlpatterns = [
	path("lecturers/", views.LecturerView.as_view()),
	path("material/", views.MaterialView.as_view()),
	path("subjects/", views.SubjectsView.as_view()),
	path("programmes/", views.ProgrammeView.as_view()),
	path("user/", views.UserDetail.as_view())
]
