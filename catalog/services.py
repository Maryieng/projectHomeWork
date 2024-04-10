from django.conf import settings
from django.core.cache import cache

from catalog.models import Product, Category


def get_cached_categories():
    if settings.CACHES_ENABLED:
        key = 'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.all()
    return categories_list


def get_cached_products():
    if settings.CACHES_ENABLED:
        key = 'products_list'
        products_list = cache.get(key)
        if products_list is None:
            products_list = Product.objects.all()
            cache.set(key, products_list)
    else:
        products_list = Product.objects.all()
    return products_list
