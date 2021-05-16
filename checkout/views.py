from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
import json

from earrings.models import Earring

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