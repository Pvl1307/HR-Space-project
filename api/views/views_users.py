from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.serailizers.serializers_users import UserCreateSerializer, UserSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
