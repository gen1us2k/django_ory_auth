from django.conf import settings

def processor(request):
    logout_url = ""

    if request.user.is_authenticated:
        if hasattr(request.user, "ory_logout_url"):
            logout_url = request.user.ory_logout_url

    context = {
        'login_url': f"{settings.ORY_UI_URL}/login",
        'signup_url': f"{settings.ORY_UI_URL}/registration",
        'logout_url': logout_url,
        'recovery_url': f"{settings.ORY_UI_URL}/recovery",
        'verify_url': f"{settings.ORY_UI_URL}/verification",
        'profile_url': f"{settings.ORY_UI_URL}/settings",
    }

    return context

