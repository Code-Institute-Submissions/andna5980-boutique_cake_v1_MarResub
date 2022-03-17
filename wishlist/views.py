from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product

from django.contrib import messages
from .models import Wishlist

@login_required
def wishlist(request):
    """
    View to render user wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)

    def __len__(self):
        """ add items in wishlist """
        return sum(item['quantity'] for item in self.wishlist.values()) 

@login_required
def add_to_wishlist(request, product_id):
    """
    Any logged user can add any product
    to the wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    wishlist, _= Wishlist.objects.get_or_create(user=request.user)

    wishlist.products.add(product)
    messages.info(request, 'You have a new product added to your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Any logged user can remove any product
    from the wishlist
    """
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    #Remmove product from wishlist
    wishlist.products.remove(product)
    messages.info(request, 'Product removed from your wishlist')

    return redirect(request.META.get('HTTP_REFERER'))