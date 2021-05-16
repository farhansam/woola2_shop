from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<earring_id>', add_to_cart, name='add_to_cart'),
    path('remove/<earring_id>', remove_from_cart, name='remove_from_cart')
]