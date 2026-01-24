from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from .models import ProductVariant, Category, Product
from cart.forms import AddToCartForm
from cart.cart import Cart

def catalog(request):
    categories = Category.objects.all()
    products = (
        Product.objects.select_related("category")
        .filter(variants__isnull=False)
        .prefetch_related(
            Prefetch(
                "variants",
                queryset=ProductVariant.objects.order_by("price"),
                to_attr="first_variant_list",
            )
        )
        .distinct()
        .order_by("name")
    )
    current_category = "all"
    category_slug = request.GET.get("category")
    if category_slug and category_slug != "all":
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        current_category = category.slug

    paginator = Paginator(products, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "catalog/catalog.html",
        {
            "categories": categories,
            "page_obj": page_obj,
            "current_category": current_category,
        },
    )


def product_detail(request, product_slug):
    product = get_object_or_404(
        Product.objects.prefetch_related("variants", "variants__color","variants__size"),
        slug=product_slug,
    )
    variants = product.variants.all()
    if not variants.exists():
        raise Http404("Нет вариантов товара")
    current_variant = variants.first()
    available_size_color_combinations = {}
    for variant in variants:
        size = variant.size.id
        color = variant.color.id
        if size not in available_size_color_combinations:
            available_size_color_combinations[size] = []
        available_size_color_combinations[size].append(color)

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
            cart = Cart(request)
            cart.add(product_variant=variant, quantity=quantity)

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
            "variant": current_variant,
            "available_size_color_combinations": available_size_color_combinations,
            "form": form,
        },
    )


def get_variant(request, product_id):
    size_id = request.GET.get("size")
    color_id = request.GET.get("color")

    variant = get_object_or_404(
        ProductVariant,
        product_id=product_id,
        size__id=size_id,
        color__id=color_id
    )

    return JsonResponse({
        "image": variant.image.url if variant.image else None,
        "price": str(variant.price),
        "price_with_discount": str(variant.price_with_discount) if variant.price_with_discount else None,
    })
