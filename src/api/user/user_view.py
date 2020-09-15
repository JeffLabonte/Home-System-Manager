from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.user.user_serializer import UserSerializer


class UserViewsets(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
