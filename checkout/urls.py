from django.urls import path
from .views import checkout, payment_completed, checkout_success, checkout_cancel

urlpatterns = [
    path('', checkout, name='checkout_route'),
    path('payment_completed/', payment_completed, name='payment_completed_route'),
    path('checkout_success/', checkout_success, name='checkout_success_route'),
    path('checkout_cancel/', checkout_cancel, name='checkout_cancel_route')
]