from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.index),
    path('create/', products.views.create_product)
]
