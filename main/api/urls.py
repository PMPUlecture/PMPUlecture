from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^programmes/$', views.ProgListView.as_view()),
#     url(r'^subjects/$', views.SubjectView.as_view()),
    path('lecturer/', views.DetailLecturer.as_view()),
    path('struct/', views.ListUsers.as_view()),
    ]