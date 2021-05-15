from django.urls import path
import earrings.views

urlpatterns = [
    path('', earrings.views.index),
    path('create/', earrings.views.create_earring),
    path('update/<earring_id>', earrings.views.update_earring, name='update_earring_route')
]
