from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from .tasks import send_email_new_user

User = get_user_model()


class SignUp(generics.CreateAPIView):
    """Регистрация пользователя и отправка сообщения"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        send_email_new_user.delay(user.id)
