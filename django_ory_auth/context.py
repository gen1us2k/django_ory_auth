import requests
from django.conf import settings
from django.core.cache import cache

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
        cache_key = f"logout_{request.COOKIES.get('sessionid')}"
        logout_url = cache.get(cache_key)
        if not logout_url:
            r = requests.get(
                f"{settings.ORY_SDK_URL}/self-service/logout/browser",
                cookies=request.COOKIES
            )
            logout_url = r.json().get('logout_url')
            cache.set(cache_key, logout_url, timeout=900) # Cache for 15 minutes

        context["logout_url"] = logout_url

    return context

