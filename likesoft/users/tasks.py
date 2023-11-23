from likesoft.celery import app

from .service import send


@app.task
def send_email_new_user(user_id):
    send(user_id)
