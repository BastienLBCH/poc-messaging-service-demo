from django.conf import settings
from django.http import HttpResponse
from rest_framework import status
import jwt


keycloak_public_key = settings.KEYCLOAK_PUBLIC_KEY
keycloak_alg = settings.KEYCLOAK_ALG


class JWTAuthentificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """
        Middleware verifying each request is identified
        If user is authentified execute view normally, else returns http error 401
        :param request:
        :return:
        """

        try:
            name, bearer = request.headers["Authorization"].split(" ")
            if name != "Bearer":
                raise Exception

            payload = None
            key = '-----BEGIN PUBLIC KEY-----\n' + keycloak_public_key + '\n-----END PUBLIC KEY-----'

            payload = jwt.decode(
                bearer,
                key,
                algorithms=keycloak_alg,
                audience="account"
            )
        except Exception:
            return HttpResponse("User is not correctly authentified", status=status.HTTP_401_UNAUTHORIZED)

        response = self.get_response(request)

        return response

