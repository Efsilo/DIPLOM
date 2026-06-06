from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_task(subject, message, recipient_list):
    """
    Асинхронная отправка email через Celery.
    Используется для подтверждения регистрации и других уведомлений.
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        fail_silently=False,
    )

@shared_task
def send_order_confirmation(order_id, user_email):
    """
    Асинхронная отправка подтверждения заказа.
    Вызывается после успешного оформления заказа.
    """
    subject = f"Ваш заказ №{order_id} принят"
    message = f"Спасибо за покупку! Ваш заказ №{order_id} успешно оформлен и передан в обработку."
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )