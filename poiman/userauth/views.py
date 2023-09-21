from django.shortcuts import render
from django.conf import settings
import jwt
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework import generics
from .models import AppUser
from rest_framework.permissions import AllowAny


# Create your views here.


def get_payload(request):
        """
        This function will take token from `Authorization`, 
        and decode the payload and send the payload back 
        to any function where this function is used.
        """
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            jwt_token=  auth_header.split(' ')[1]
        else:
            return None
        try:
            # Decode the JWT token
            decoded_payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            return Response({'detail': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response({'detail': 'Token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer