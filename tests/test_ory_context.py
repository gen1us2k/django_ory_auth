import pytest


@pytest.mark.vcr
def test_context_processor_unauthenticated(django_user_model, client, rf):
    client.cookies['ory_kratos_session'] = 'MTY1MTY3OTc5N3xEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJR3BrZDAxeVFVcGlTVWxYVVc1UmFtUTNWVTFXUlZSTVZHRjRkVkF3TVhseHzeW6gJiLTLfJGAYPe4Bk44r0WtQIuZLQexqo0ZmMjoFw=='
    response = client.get("/home")

    assert response.status_code == 200
    assert response.context["login_url"] == "http://127.0.0.1:4455/login"
    assert response.context["signup_url"] == "http://127.0.0.1:4455/registration"
    assert response.context["recovery_url"] == "http://127.0.0.1:4455/recovery"
    assert response.context["verify_url"] == "http://127.0.0.1:4455/verification"
    assert response.context["profile_url"] == "http://127.0.0.1:4455/settings"
    assert response.context["logout_url"] == ""


@pytest.mark.vcr
def test_context_processor_authenticated(django_user_model, client, rf):
    client.cookies['ory_kratos_session'] = 'MTY1MTc3MzE0OXxEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJR2M1TUdwa1dWQnlZMEpRYURaWWIxQjNTbTEwV1VKM1pXa3hTR2c0WkROMXyM5gb29-mKbogcj_cY5Zv6O4hkhPuzd257XJO8qarKDQ=='
    response = client.get("/home")

    assert response.status_code == 200
    assert response.context["login_url"] == "http://127.0.0.1:4455/login"
    assert response.context["signup_url"] == "http://127.0.0.1:4455/registration"
    assert response.context["recovery_url"] == "http://127.0.0.1:4455/recovery"
    assert response.context["verify_url"] == "http://127.0.0.1:4455/verification"
    assert response.context["profile_url"] == "http://127.0.0.1:4455/settings"
    assert response.context["logout_url"] == "http://127.0.0.1:4433/self-service/logout?token=4EWguJ7ppTSUNm80o8YGEBKFWyc36AVY"



