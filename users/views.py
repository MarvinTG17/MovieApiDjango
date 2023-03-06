from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @csrf_exempt
    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))