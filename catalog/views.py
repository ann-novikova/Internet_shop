from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import ContactInfo, Product


def home(request):
    latest_products = Product.objects.order_by("-created_at")[:5]  # Последние 5 продуктов
    print("Latest products:")
    for product in latest_products:
        print(f"- {product.name}")
    context = {"latest_products": latest_products}
    return render(request, "home.html", context)


def contact(request):
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
