import requests

from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.core.cache import cache
from .apps import config

UserModel = get_user_model()
HTTP_STATUS_OK = 200
HTTP_STATUS_UNAUTHORIZED = 401

class OryBackend(BaseBackend):
    def authenticate(self, request):
        cache_key = f"userid_{request.COOKIES.get('sessionid')}"
        user_id = cache.get(cache_key)
        if not user_id:
            sdk_url = config().get('ORY_SDK_URL')
            sess = requests.get(
                f"{sdk_url}/sessions/whoami",
                cookies=request.COOKIES
            )
            if sess.status_code != HTTP_STATUS_OK:
                return None
            user_id = sess.json().get('identity', {}).get('id', None)
            if user_id:
                cache.set(cache_key, user_id, timeout=300) # Cache for 5 minutes
        
        if not user_id:
            return None
            
        user, created = UserModel._default_manager.get_or_create(
            **{UserModel.USERNAME_FIELD: user_id}
        )

        return user

