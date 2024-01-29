from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from furniture.models import Product
from .cart import Cart
from .forms import CartAddForm

@require_POST
def cart_add(request , id):
    cart = Cart(request)
    form = CartAddForm(request.POST)
    product = get_object_or_404(Product , id = id)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'], 
                 override_quantity=['override'])
    
    return redirect('cart:cart_view')

@require_POST
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = id)
    cart.remove(product)

    return redirect('cart:cart_view')

def cart_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddForm(initial = {'quantity':item['quantity'],
                                                              'override':True})
    return render(request, 'cart/cart.html', {'cart':cart})