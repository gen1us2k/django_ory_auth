import requests
from django.conf import settings


def processor(request):
    context = {
        'login_url': f"{settings.ORY_UI_URL}/login",
        'signup_url': f"{settings.ORY_UI_URL}/registration",
        'logout_url': "",
        'recovery_url': f"{settings.ORY_UI_URL}/recovery",
        'verify_url': f"{settings.ORY_UI_URL}/verification",
        'profile_url': f"{settings.ORY_UI_URL}/settings",
    }
    # Only make this request for users authenticated via Ory. 
    # Local users will have the email field set, but not users in Ory
    if request.user.is_authenticated and not request.user.email:
        r = requests.get(
            f"{settings.ORY_SDK_URL}/self-service/logout/browser",
            cookies=request.COOKIES
        )

        context["logout_url"] = r.json().get('logout_url')

    return context

