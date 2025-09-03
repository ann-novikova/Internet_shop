from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import ContactInfo, Product


def home(request):
    """Контроллер, который будет обрабатывает запросы по пути Home."""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)

def product_details(request, pk):
    """Контроллер, который будет обрабатывает запросы по пути product_details."""
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_details.html", context)


def contact(request):
    """Контроллер, который будет обрабатывает запросы по пути Сontact."""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    try:
        contact_info = ContactInfo.objects.all()
    except ContactInfo.DoesNotExist:
        contact_info = None
    context = {"contact_info": contact_info}
    return render(request, "contacts.html", context)
