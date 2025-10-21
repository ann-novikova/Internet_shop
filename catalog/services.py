from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category=category_id)
    products = cache.get("products_by_category")
    if products is not None:
        return products
    products = Product.objects.filter(category=category_id)
    cache.set("products_by_category", products)
    return products