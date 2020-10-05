from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from text_saver_admaren.responses import serializer_error_response
from user.serializers import UserLoginSerializer


class UserLoginView(APIView):
    '''
    The user login API works such a way that, JWT token is generated if the user already and the credentials authenticated.
    A new user will be created if no user exists with the existing credentials
    '''

    @permission_classes((AllowAny,))
    def post(self, request):
        # user request data(email and password)
        data = request.data
        serializer = UserLoginSerializer(data=data)
        # checking request validation
        if serializer.is_valid():
            # creating user
            user = serializer.save()
            # generating JWT token for user
            refresh_token = RefreshToken.for_user(user=user)
            return Response({
                'success': True,
                'message': 'User successfully logged in',
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token),
            },
                status=status.HTTP_200_OK
            )
        # error response if request data is invalid
        return serializer_error_response(serializer.errors)
