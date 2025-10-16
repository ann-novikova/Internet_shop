from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Контроллер для рендеринга списка товаров"""
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для рендеринга конкретного товара"""
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания товара"""
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования товара"""
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления товара"""
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


class ContactView(LoginRequiredMixin, TemplateView):
    """Контроллер для страницы контакты"""
    template_name = "contacts.html"
