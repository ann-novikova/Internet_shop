from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, home, product_details

app_name = CatalogConfig.name


urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contact, name="contact"),
    path("products/<int:pk>/", product_details, name="product_details"),
]
