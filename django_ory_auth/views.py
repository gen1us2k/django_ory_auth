from django.contrib.auth import login as contrib_auth_login
from django.shortcuts import redirect
from django.contrib.auth import logout as contrib_auth_logout
from django.conf import settings

from .middleware import get_user

def login(request, user, backend=None):
    """
    Logs a user in
    """
    user = get_user(request)
    if user is not None:
        contrib_auth_login(request, user)

    return redirect(settings.LOGIN_REDIRECT_URL)

def logout(request):
    """
    View that clears cached auth data. Configure Ory to redirect here
    on log out.
    """
    if hasattr(request, "_cached_user"):
        delattr(request, "_cached_user")

    contrib_auth_logout(request)

    return redirect(settings.LOGOUT_REDIRECT_URL)
