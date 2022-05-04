import pytest

from ory_auth.backend import OryBackend
from django.test import RequestFactory

@pytest.mark.vcr
def test_unauthenticated(django_user_model):
    req = RequestFactory().get("/")
    user = OryBackend().authenticate(req)
    assert user is None

@pytest.mark.vcr
def test_authenticated(django_user_model):
    req = RequestFactory().get("/")
    req.COOKIES['ory_kratos_session'] = 'MTY1MTY3OTc5N3xEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJR3BrZDAxeVFVcGlTVWxYVVc1UmFtUTNWVTFXUlZSTVZHRjRkVkF3TVhseHzeW6gJiLTLfJGAYPe4Bk44r0WtQIuZLQexqo0ZmMjoFw=='
    user = OryBackend().authenticate(req)

    assert user is not None
    assert user.username == 'e669049e-8a0a-4d7f-b0dd-b9e1f38cfcb8'
