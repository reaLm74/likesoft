from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer
from .tasks import send_email_new_user

User = get_user_model()


class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Отправка сообщения после регистраций на веб сервисе"""
        user = serializer.save()
        send_email_new_user.delay(user.id)
