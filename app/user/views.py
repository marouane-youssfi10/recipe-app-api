from .serializers import UserSerializer
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    """Create a new user is the system"""
    serializer_class = UserSerializer


