from ory_auth.backend import OryBackend
from django.test import RequestFactory

def test_unauthenticated(django_user_model):
    req = RequestFactory().get("/")
    user = OryBackend().authenticate(req)
    assert user is None


