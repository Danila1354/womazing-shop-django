from django.shortcuts import render

# Create your views here.
from .models import ProductVariant, Category
from django.core.paginator import Paginator


def catalog(request):
    products = ProductVariant.objects.select_related(
        "product", "color", "category"
    ).all()
    categories = Category.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "catalog/catalog.html",
        {"categories": categories, "page_obj": page_obj},
    )


def product_detail(request, pk):
    product = ProductVariant.objects.select_related(
        "product", "color", "category"
    ).get(pk=pk)
    return render(request, "catalog/product_detail.html", {"product": product})