from django.shortcuts import render, redirect

from .forms import UserInfoForm
from cart.cart import Cart


def checkout(request):
    cart = Cart(request)
    form = UserInfoForm()
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders:confirm_order")

    return render(request, "orders/checkout.html", {"cart": cart, "form": form})


def confirm_order(request):
    return render(request, "orders/confirm-order.html")
