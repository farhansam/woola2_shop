from django.urls import path
import earrings.views

urlpatterns = [
    path('', earrings.views.index, name='show_earring_route'),
    path('create/', earrings.views.create_earring),
    path('update/<earring_id>', earrings.views.update_earring, name='update_earring_route'),
    path('delete/<earring_id>', earrings.views.delete_earring, name='delete_earring_route')
]
