from django.shortcuts import render, redirect

from django.http import Http404, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .models import User


class RedirectIfLogin(View):
    def get(self, request, *args, **kwargs):
        return redirect('/')


class LogInView(View):
    def get(self, request, *args, **kwargs):
        return 'no'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/?error=1')


class LogOutView(View):
    def get(self, request, *args, **kwargs):
        print("herer")
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
