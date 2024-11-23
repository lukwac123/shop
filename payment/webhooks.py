import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe.error
from orders.models import Order
from .tasks import payment_completed

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Niepoprawny ładunek danych.
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Niepoprawna sygnatura.
        return HttpResponse(status=400)
    
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # Oznaczenie zamówienia jako zapłaconego.
            order.paid = True
            # Zapisanie identyfikatora płatności Stripe.
            order.stripe_id = session.payment_intent
            order.save()
            # Uruchomienie zadania asynchronicznego.
            payment_completed.delay(order.id)

    return HttpResponse(status=200)
