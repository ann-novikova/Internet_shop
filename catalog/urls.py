from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactView, ListProductsCategoryDetailView, ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView, ProductUpdateView)

app_name = CatalogConfig.name


urlpatterns = [
    path("products/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contact"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_details"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/<int:pk>/", ListProductsCategoryDetailView.as_view(), name="category_product"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
