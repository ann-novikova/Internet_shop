from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
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

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования товара"""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер для удаления товара"""

    permission_required = "catalog.delete_product"
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


class ContactView(LoginRequiredMixin, TemplateView):
    """Контроллер для страницы контакты"""

    template_name = "contacts.html"
