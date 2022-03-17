from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    """
    Model shows all products/items in the wishlist 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                        through="WishlistItem",
                                        related_name='product_wishlists')

    def __str__(self):
        return Wishlist, f'({self.user})'
   

class WishlistItem(models.Model):
    """
    'through' model allow users to add products to wishlist
    """

    product = models.ForeignKey(Product,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist,
                                null=False,
                                blank=False,
                                 on_delete=models.CASCADE)

def __str__(self):
    return self.product.name                                 