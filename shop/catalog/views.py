from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import ProductVariant, Category, Product
from .forms import AddToCartForm


def catalog(request):
    categories = Category.objects.all()
    products = (
        Product.objects.select_related("category")
        .prefetch_related("variants", "variants__color")
        .all()
        .order_by("name")
    )
    current_category = 'all'
    if request.GET.get("category"):
        if request.GET["category"] != "all":
            current_category = get_object_or_404(Category, slug=request.GET["category"]).slug
            products = products.filter(category__slug=request.GET["category"])

    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "catalog/catalog.html",
        {
            "categories": categories, 
            "page_obj": page_obj,
            'current_category': current_category,
        },
    )


def product_detail(request, product_slug):
    product = get_object_or_404(
        Product.objects.prefetch_related("variants", "variants__color"), slug=product_slug
    )

    variants = product.variants.all()
    if not variants.exists():
        raise Http404("Нет вариантов товара")
    current_variant = variants.first()

    form = AddToCartForm(
        product=product,
        initial={
            "size": current_variant.size,
            "color": current_variant.color,
            "quantity": 1,
        },
    )
    if request.method == "POST":
        form = AddToCartForm(request.POST, product=product)
        if form.is_valid():
            size = form.cleaned_data["size"]
            color = form.cleaned_data["color"]
            quantity = form.cleaned_data["quantity"]

            variant = ProductVariant.objects.get(
                product=product, size=size, color=color
            )
            # TODO: Add the variant to the cart

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
            "variant": current_variant,
            "form": form,
        },
    )
