from django.urls import include, path

from .views import logout

urlpatterns = [
    path("_logout", logout, name="logout_cache"),
]
