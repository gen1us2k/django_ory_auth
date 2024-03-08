from django.urls import include, path

from .views import logout, login

urlpatterns = [
    path("_login", login, name="ory_login"),
    path("_logout", logout, name="ory_logout"),
]
