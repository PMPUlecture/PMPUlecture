from django.shortcuts import redirect


def auth_allowed(backend, details, response, **kwargs):
    if not backend.auth_allowed(response, details):
        return redirect('/login/?error=2')