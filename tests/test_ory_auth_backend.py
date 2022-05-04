import pytest

from ory_auth.backend import OryBackend

@pytest.mark.vcr
def test_unauthenticated(rf):
    req = rf.get("/")
    user = OryBackend().authenticate(req)
    assert user is None

@pytest.mark.vcr
def test_authenticated(rf, django_user_model):
    req = rf.get("/")
    req.COOKIES['ory_kratos_session'] = 'MTY1MTY3OTc5N3xEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJR3BrZDAxeVFVcGlTVWxYVVc1UmFtUTNWVTFXUlZSTVZHRjRkVkF3TVhseHzeW6gJiLTLfJGAYPe4Bk44r0WtQIuZLQexqo0ZmMjoFw=='
    user = OryBackend().authenticate(req)

    assert user is not None
    assert user.username == 'e669049e-8a0a-4d7f-b0dd-b9e1f38cfcb8'

    u = django_user_model.objects.get(username=user.username)

    assert u is not None
