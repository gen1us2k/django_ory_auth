from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = auth.authenticate(request)
        if user:
            request.user = user
            auth.login(request, user)
