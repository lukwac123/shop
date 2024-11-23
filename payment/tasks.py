from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Zadanie wysyła e-mailem powiadomienie po pomyślnym utworzeniu zamówienia.
    """
    order = Order.objects.get(id=order_id)
    # Utworzenie wiadomości e-mail z fakturą
    subject = f'Mój sklep - faktura nr {order.id}'
    message = 'W załączniku przesyłamy fakturę dla ostatniego zakupu.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
    # Wygenerowanie dokumnetu PDF.
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # Dołączanie pliku w formacie PDF.
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # Wysyłanie wiadomości e-mail
    email.send()