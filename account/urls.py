from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LogInView.as_view()),
]
