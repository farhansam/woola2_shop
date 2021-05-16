from django.urls import path
from .views import checkout, payment_completed

urlpatterns = [
    path('', checkout, name='checkout_route'),
    path('payment_completed/', payment_completed, name='payment_completed_route')
]