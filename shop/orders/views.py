from django.shortcuts import render

from .forms import UserInfoForm
from cart.cart import Cart


def checkout(request):
    cart = Cart(request)
    form = UserInfoForm()
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, "orders/checkout.html", {"cart": cart, "form": form})
