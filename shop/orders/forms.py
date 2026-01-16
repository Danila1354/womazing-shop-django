from django import forms
from .models import Order


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "name",
            "email",
            "phone",
            "country",
            "city",
            "street",
            "house",
            "apartment",
            "payment_method",
            "comment",
        ]
        widgets = {
            "payment_method": forms.RadioSelect,
        }
