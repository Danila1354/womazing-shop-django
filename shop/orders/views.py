from django.shortcuts import render

from .forms import UserInfoForm

def checkout(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            print(name,email,phone)
            # (Further processing logic goes here)
    return render(request, "orders/checkout.html", {})
    