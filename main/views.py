from django.shortcuts import render, redirect
from django.conf import settings


def index(request):
    #if request.META.get('wsgi.url_scheme') == 'https' and not settings.DEBUG:
    #    return redirect('http://' + request.META.get('HTTP_HOST') + request.path)

    return render(request, 'index.html', context={'user': request.user})
