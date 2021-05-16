from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from earrings.models import Earring

# Create your views here.
def add_to_cart(request, earring_id):
    cart = request.session.get('shopping_cart', {})
    
    if earring_id not in cart:
        earring = get_object_or_404(Earring, pk=earring_id)
        cart[earring_id] = {
            'id': earring_id,
            'name': earring.name,
            'price': earring.price,
            'qty': 1
        } 
        
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Item has been added to your cart!")
        return redirect(reverse('show_earring_route'))
    else:
        cart[earring_id]['qty'] +=1
        request.session['shopping_cart'] = cart
        return redirect(reverse('show_earring_route'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    print(cart)
    return render(request, 'cart/view_cart-template.html', {
        'shopping_cart':cart
    })


def remove_from_cart(request, earring_id):
    cart = request.session.get('shopping_cart',{})
    
    if earring_id in cart:
        del cart[earring_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart!")
        
    return redirect(reverse('view_cart'))