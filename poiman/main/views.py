from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework import exceptions
import jwt
from userauth.views import get_payload
from userauth.models import AppUser


class ProtectedView(APIView):
    """
    This is a sample view which is protected by JWT token
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        decoded_payload = get_payload(request)
        user_id = decoded_payload['user_id']
        user = AppUser.objects.filter(id=user_id).first()
        context = {'user_id': user_id,
                  'email': user.email,
                  }
        if user.is_superuser:
            context['admin'] = True
        return Response(context, status=status.HTTP_200_OK)
        
    