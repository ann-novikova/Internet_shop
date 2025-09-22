from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "category", "photo", "description", "price"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "category", "photo", "description", "price"]
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ContactView(TemplateView):
    template_name = "contacts.html"
