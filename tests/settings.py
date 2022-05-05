from django.contrib.auth.decorators import login_required
from django.urls import path
from django.http import JsonResponse
from django.shortcuts import render

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mem_db"
    }
}
SECRET_KEY = 'somethingnotsecureatall'
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django_ory_auth"
]

AUTHENTICATION_BACKENDS = [
    "django_ory_auth.backend.OryBackend",
]

ORY_UI_URL = "http://127.0.0.1:4455"
ORY_SDK_URL = "http://127.0.0.1:4433"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_ory_auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'tests/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_ory_auth.context.processor',
            ],
        },
    },
]

ROOT_URLCONF = __name__


@login_required
def json_home(request):
    return JsonResponse({"message": "hello"})

def home_html(request):
    return render(request, "home.html", {})


urlpatterns = [
    path("", json_home),
    path("home", home_html)
]
