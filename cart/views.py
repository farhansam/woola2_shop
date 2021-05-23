from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from earrings.models import Earring

# Create your views here.


@login_required
def add_to_cart(request, earring_id):
    cart = request.session.get('shopping_cart', {})
    
    if earring_id not in cart:
        earring = get_object_or_404(Earring, pk=earring_id)
        cart[earring_id] = {
            'id': earring_id,
            'name': earring.name,
            'price': float(earring.price),
            'image': str(earring.image),
            'qty': 1,
            'sub_total': float(earring.price)
        } 
        
        request.session['shopping_cart'] = cart
        messages.success(request, "Item has been added to your cart!")
        return redirect(reverse('show_earring_route'))
    else:
        cart[earring_id]['qty'] +=1
        cart[earring_id]['sub_total'] = round((float(cart[earring_id]['qty']) * float(cart[earring_id]['price'])), 2)
        request.session['shopping_cart'] = cart
        messages.success(request, "Item has been added to your cart!")
        return redirect(reverse('show_earring_route'))


@login_required
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    print(cart)
    return render(request, 'cart/view_cart-template.html', {
        'shopping_cart':cart
    })


@login_required
def remove_from_cart(request, earring_id):
    cart = request.session.get('shopping_cart',{})
    
    if earring_id in cart:
        del cart[earring_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart!")
        
    return redirect(reverse('view_cart_route'))


@login_required
def update_quantity(request, earring_id):
    cart = request.session.get('shopping_cart', {})
    if earring_id in cart:
        cart[earring_id]['qty'] = request.POST['qty']
        cart[earring_id]['sub_total'] = round((float(cart[earring_id]['qty']) * float(cart[earring_id]['price'])), 2)
        request.session['shopping_cart'] = cart
        messages.success(request, f"Quantity for {cart[earring_id]['name']} has been changed")
    
    return redirect(reverse('view_cart_route'))