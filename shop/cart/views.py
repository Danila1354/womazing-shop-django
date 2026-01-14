from django.shortcuts import render, get_object_or_404,redirect

from .cart import Cart
from .forms import UpdateCartForm
from catalog.models import ProductVariant


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart.html", {"cart": cart})


def cart_update(request, variant_id):
    cart = Cart(request)
    product = get_object_or_404(ProductVariant, id=variant_id)
    form = UpdateCartForm(request.POST)
    if form.is_valid():
        cart.add(product, form.cleaned_data["quantity"], True)

    return redirect("cart:cart_detail")
