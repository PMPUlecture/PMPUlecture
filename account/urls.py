from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.LogOutView.as_view()),
    path('', include('social_django.urls', namespace='social')),
]
