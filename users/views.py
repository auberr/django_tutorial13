from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer



# Create your views here.
class UserView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPariView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청")