from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny 
from rest_framework.authtoken.models import Token

class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]  # Permite acesso público a este endpoint

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Cria o token para o novo usuário
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, * args, **kwargs):
        user = User.objects.all()
        serialize = UserSerializer(user, many = True)
        return Response(serialize.data, status=status.HTTP_200_OK)