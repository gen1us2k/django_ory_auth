import requests

from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from .apps import config

UserModel = get_user_model()
HTTP_STATUS_OK = 200
HTTP_STATUS_UNAUTHORIZED = 401

class OryBackend(BaseBackend):
    def authenticate(self, request):
        print("HERE")
        sdk_url = config().get('ORY_SDK_URL')
        sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
        if sess.status_code != HTTP_STATUS_OK:
            return None
        user_id = sess.json().get('identity', {}).get('id', None)
        if not user_id:
            return None
        user, created = UserModel._default_manager.get_or_create(
            **{UserModel.USERNAME_FIELD: user_id}
        )

        return user

