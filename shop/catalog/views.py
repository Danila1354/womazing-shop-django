from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import ProductVariant, Category, Product
from .forms import AddToCartForm



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
    product = get_object_or_404(
        Product.objects.prefetch_related(
            "variants__color", "variants__category"
        ),
        pk=pk
    )
    form = AddToCartForm(product=product)
    if request.method == "POST":
        form = AddToCartForm(request.POST, product=product)
        if form.is_valid():
            size = form.cleaned_data["size"]
            color = form.cleaned_data["color"]
            quantity = form.cleaned_data["quantity"]

            variant = ProductVariant.objects.get(
                product=product,
                size=size,
                color=color
            )
            # TODO: Add the variant to the cart

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
            "form": form,
        },
    )
