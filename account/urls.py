from django.urls import path
from . import views

urlpatterns = [
    path('', views.RedirectIfLogin.as_view()),
    path('login', views.LogInView.as_view()),
    path('login/', views.LogInView.as_view()),
    path('logout', views.LogOutView.as_view()),
    path('logout/', views.LogOutView.as_view()),
]
