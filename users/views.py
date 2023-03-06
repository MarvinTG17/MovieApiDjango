from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import requires_csrf_token

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @requires_csrf_token
    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))