from rest_framework import generics

from user.serializers import UserSerializar


class CreateUserView(generics.CreateAPIView):
    """Create a user in the system"""
    serializer_class = UserSerializar
