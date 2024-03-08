import requests

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from .apps import config

UserModel = get_user_model()
HTTP_STATUS_OK = 200
HTTP_STATUS_UNAUTHORIZED = 401

class OryBackend(BaseBackend):
    def _fetch_remote_session(self, request):
        """
        Network call to get the remote user session.
        :param request:
        :return:
        """
        sdk_url = config().get('ORY_SDK_URL')
        sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
        if sess.status_code != HTTP_STATUS_OK:
            return {}
        return sess.json() or {}

    def _fetch_logout_url(self, request):
        """
        Make a network request for the logout URL
        :param request:
        :return:
        """
        r = requests.get(
            f"{config().get('ORY_SDK_URL')}/self-service/logout/browser",
            cookies=request.COOKIES
        )
        return r.json().get('logout_url')

    def authenticate(self, request):
        """
        Validate the user remotely and return a user, creating it if
        it doesn't exist on our side.
        :param request:
        :return: User
        """
        remote_session = self._fetch_remote_session(request)
        user_id = remote_session.get('identity', {}).get('id', None)

        if not user_id:
            return None

        user, _ = UserModel._default_manager.get_or_create(
            **{UserModel.USERNAME_FIELD: user_id}
        )

        logout_url = self._fetch_logout_url(request)
        user.ory_logout_url = logout_url

        user.backend = self
        return user
