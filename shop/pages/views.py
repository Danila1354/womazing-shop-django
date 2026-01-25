from django.shortcuts import render
from django.db.models import Prefetch
from catalog.models import ProductVariant, Product
from .forms import ContactMessageForm
import random


def home(request):
    product_ids = list(Product.objects.filter(variants__is_new_collection=True).distinct().values_list('id', flat=True))
    
    random_ids = random.sample(product_ids, min(len(product_ids), 3))
    
    new_products = (
        Product.objects.filter(id__in=random_ids)
        .select_related("category")
        .prefetch_related(
            Prefetch(
                "variants",
                queryset=ProductVariant.objects.filter(is_new_collection=True).order_by("price"),
                to_attr="first_variant_list",
            )
        )
    )
    
    return render(request, "pages/home.html", {"new_products": new_products})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    form = ContactMessageForm()
    success = False
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactMessageForm()
    return render(request, "pages/contact.html", {"form": form, "success": success})
