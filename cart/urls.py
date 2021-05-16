from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, update_quantity

urlpatterns = [
    path('', view_cart, name='view_cart_route'),
    path('add/<earring_id>', add_to_cart, name='add_to_cart_route'),
    path('remove/<earring_id>', remove_from_cart, name='remove_from_cart_route'),
    path('update_quantity/<earring_id>', update_quantity, name='update_quantity_route')
]