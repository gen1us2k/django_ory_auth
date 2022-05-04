import pytest
from unittest import mock

from ory_auth.middleware import AuthenticationMiddleware


@pytest.mark.vcr
def test_middleware_unauthenticated(rf):
    req = rf.get("/")

    get_response = mock.MagicMock()

    m = AuthenticationMiddleware(get_response)
    response = m(req)

    assert response == get_response.return_value


@pytest.mark.vcr
def test_middleware_authenticated(django_user_model, client, rf):
    client.cookies['ory_kratos_session'] = 'MTY1MTY3OTc5N3xEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJR3BrZDAxeVFVcGlTVWxYVVc1UmFtUTNWVTFXUlZSTVZHRjRkVkF3TVhseHzeW6gJiLTLfJGAYPe4Bk44r0WtQIuZLQexqo0ZmMjoFw=='
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


