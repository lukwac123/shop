from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Zadanie wysyłające powiadomienie za pomocą wiadomości e-mail
    po zakończonym powodzeniem utworzeniu obiektu zamówienia.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Zamówienie nr. {order_id}'
    message = f'Witaj {order.first_name},\n\nDziękujemy za złożenie zamówenia w naszym sklepie.\n\nIdentyfikator zamówienia to {order.id}.\n\n'

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])

    return mail_sent