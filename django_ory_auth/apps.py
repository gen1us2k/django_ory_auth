from django.apps import AppConfig
from django.conf import settings

class OryAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_ory_auth'


def config():
    return {
        'ORY_SDK_URL': getattr(settings, 'ORY_SDK_URL', 'http://127.0.0.1:4433'),
        'ORY_UI_URL': getattr(settings, 'ORY_UI_URL', 'http://127.0.0.1:4455'),
    }
