from django.urls import path
import earrings.views

urlpatterns = [
    path('', earrings.views.index),
    path('create/', earrings.views.create_earring)
]
