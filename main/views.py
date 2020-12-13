from django.shortcuts import render, redirect


def index(request):
    if request.META.get('wsgi.url_scheme') == 'http':
        return redirect('https://pmpulecture.herokuapp.com' + request.path)

    return render(request, 'index.html', context={'user': request.user})


