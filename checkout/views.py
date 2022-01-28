from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "theres is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form, 
        'stripe_public_key': 'pk_test_51KMt91H6xUQVSsXTZheycUjOjo5QBjGm9qH2Sp3bF6aBbW8UFBZAIXwRPLocWXHMFbLZQwERnOr1dtcM9wKI7vFx00uymRrkHg',
        'client_secret': 'test client secret',
    } 

    return render(request, template, context)