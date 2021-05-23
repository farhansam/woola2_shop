from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from earrings.models import Earring
from checkout.models import Purchase
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import stripe
import json


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_earring_ids = []

    for earring_id, earring in cart.items():
        earring_model = get_object_or_404(Earring, pk=earring_id)

        line_item = {
            "name": earring_model.name,
            "amount": int(earring_model.price * 100),
            "quantity": earring['qty'],
            "currency": "SGD",
        }

        line_items.append(line_item)

        all_earring_ids.append({
            'earring_id': earring_id,
            'qty': earring['qty']
        })

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_earring_ids": json.dumps(all_earring_ids)
        },
        mode="payment",
        success_url=settings.STRIPE_SUCCESS_URL,
        cancel_url=settings.STRIPE_CANCEL_URL
    )

    return render(request, "checkout/checkout-template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

    return HttpResponse(status=200)


def handle_payment(session):
    # print(session)
    user = get_object_or_404(User, pk=session["client_reference_id"])


    # change the metadata from string back to array
    all_earring_ids = session["metadata"]["all_earring_ids"].split(",")


    # go through each earring id
    for earring_id in all_earring_ids:
        earring_model = get_object_or_404(Earring, pk=earring_id)

        # create the purchase model
        purchase = Purchase()
        purchase.book_id = earring_model
        purchase.user_id = user
        purchase.save()


def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return render(request, 'checkout/success-template.html')


def checkout_cancel(request):
    return render(request, 'checkout/cancel-template.html')
