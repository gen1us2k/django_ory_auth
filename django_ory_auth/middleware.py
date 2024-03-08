from datetime import datetime, timedelta
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

from .apps import config
from .backend import OryBackend

LAST_AUTH_CHECK_KEY = 'LAST_AUTH_CHECK_KEY'

def get_user(request):
    must_authenticate_user = True

    if hasattr(request, "_cached_user"):
        # check if we need to reauthenticate the user again
        last_auth_check = datetime.fromisoformat(request.session.get(LAST_AUTH_CHECK_KEY, "0001-01-01T00:00:00"))
        if datetime.now() < last_auth_check + timedelta(seconds=config().get('ORY_AUTH_REFRESH_INTERVAL')):
            must_authenticate_user = False

    if must_authenticate_user:
        backend = OryBackend()
        user = backend.authenticate(request)
        if user:
            request._cached_user = user
            request.session[LAST_AUTH_CHECK_KEY] = datetime.now().isoformat()
        else:
            return None

    return request._cached_user


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The Django Ory authentication middleware requires session "
                "middleware to be installed. See django ory auth README'."
            )

        user = SimpleLazyObject(lambda: get_user(request))
        if user:
            request.user = user
