from django.shortcuts import render, redirect

from django.http import Http404
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import User


class LogInView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "login.html", context={'is_authenticated': request.user.is_authenticated})
        else:
            return render(request, "login.html", context={'user': request.user})

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", context={'error': True, 'is_authenticated': request.user.is_authenticated})