from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


@shared_task
def send(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        'Спасибо за регистрацию',
        'Спасибо за регистрацию на портале',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
