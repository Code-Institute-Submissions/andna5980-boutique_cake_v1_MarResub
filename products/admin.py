from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'review', 'created', 'active')
    search_fields = ('user', 'content')
    list_filter = ('active', 'cerated', 'updated')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)