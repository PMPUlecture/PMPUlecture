from django.shortcuts import redirect

from django.views import View
from django.contrib.auth import logout


class LogOutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(request.META.get('HTTP_REFERER') if 'HTTP_REFERER' in request.META else '/')
